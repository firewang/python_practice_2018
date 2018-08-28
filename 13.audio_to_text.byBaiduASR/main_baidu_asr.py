# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/8/8 17:32
# @Author  :  wanghuodong  
# @note    : 

from pydub.silence import split_on_silence  #静音切割
import datetime
import os,sys,math,time

#将ffmpeg的bin目录临时加入系统环境变量(并没有效果！ o(╥﹏╥)o)
#虽然加入了环境变量，但是无法使用= = why?
try:
    sys.path.append( os.path.join(os.getcwd(),"extends","bin"))
except Exception:
    sys.path.insert(os.path.join(os.getcwd(), "extends", "bin"))

# print(sys.path)
# time.sleep(50)

def BAIDU_ASR(_path, dev_pid='1537'):
    ''' 百度语音转文字
    http://ai.baidu.com/docs#/ASR-Online-Python-SDK/top
    :param _path:
    :return:
     1537  普通话(纯中文识别)   1737 英语
    '''
    from aip import AipSpeech
    APP_ID = '11649566'      #修改为你自己申请的appid
    API_KEY = 'jvnqgy3fKrMBv9ppHW1pGhG3'   #修改为你自己申请的API_KEY
    SECRET_KEY = 'ujG5swFnXG3i3GmYDStA6xGoGGtsO20N'  #修改为你自己申请的SECRET_KEY
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.asr(get_file_content(_path), 'pcm', 16000, {
        'dev_pid': dev_pid,
    })
    # print(result.get('err_msg'))
    # print(result.get('err_no'))
    if result.get('err_msg') == "success.":
        return result.get('result')[0]
    else:
        return  "未正确识别error{}".format(result.get('err_no'))

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# print(BAIDU_ASR("./16K.wav"))
from pydub import AudioSegment


#根目录
base_path = os.path.join(os.getcwd())

#用来存放 extends 文件，主要是ffmpeg
extends_path = os.path.join(base_path,"extends")
if not os.path.exists(extends_path): os.mkdir(extends_path)


#用来存放原始文件 flv, avi, mp3，MP4等
raw_file_path = os.path.join(base_path,"raw_file_path")
if not os.path.exists(raw_file_path): os.mkdir(raw_file_path)

#用来存储格式已经转换好的 wav 音频文件
audio_path = os.path.join(base_path,"audio_files")
if not os.path.exists(audio_path): os.mkdir(audio_path)

#存放 输出文本文件的目录
result_path = os.path.join(base_path,"result")
if not os.path.exists(result_path): os.mkdir(result_path)

#临时存储 中间临时文件的目录，处理完成后中间文件将被清除
tmp_path = os.path.join(base_path,"tmp_path")
if not os.path.exists(tmp_path): os.mkdir(tmp_path)

def file_2_wav(raw_file_path = raw_file_path,audio_path = audio_path):
    #待转换文件名 列表
    raw_file_names = os.listdir(raw_file_path)
    for raw_file_name in raw_file_names:
        #构建输入文件完整路径
        file_path = os.path.join(raw_file_path,raw_file_name)
        print(file_path)
        #构建输出文件完成路径
        out_file_path = os.path.join(audio_path,"{}.wav".format(os.path.splitext(raw_file_name)[0]))
        print(out_file_path)

        print(os.path.splitext(raw_file_name)[1])
        #！判断文件后缀然后根据不同后缀进行不同转换
        if os.path.splitext(raw_file_name)[1] == ".mp3":
            try:
                #构建转换命令
                command = 'ffmpeg -y  -i {}  -acodec pcm_s16le -ac 1 -ar 16000 {}  '.format(file_path,out_file_path)
                #执行转换
                os.system(command)
            except Exception as e:
                #将未转换成功的文件名存储下来
                with open("./error_info.txt","a") as f:
                    f.writelines("{}--{}--转化为wav Failed".format(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"),
                                                         raw_file_name))
        else:
            #对于其他格式文件做不同操作（似乎也没有问题？？）
            try:
                #构建转换命令
                command = 'ffmpeg -y  -i {}  -acodec pcm_s16le -ac 1 -ar 16000 {}  '.format(file_path,out_file_path)
                #执行转换
                os.system(command)
            except Exception as e:
                #将未转换成功的文件名存储下来
                with open("./error_info.txt","a") as f:
                    f.writelines("{}--{}--转化为wav Failed".format(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"),
                                                         raw_file_name))

def main_trans(file_path,dev_pid='1537'):
    '''
    传入需要转文本的音频所在的目录（为已经转过格式的音频）
    :param file_path: 音频所在目录
    :param dev_pid: 指定转换为 中文格式
    :return:
    '''
    #获得输入音频文件列表
    file_names = os.listdir(file_path)
    for file_name in file_names:
        # file_name = "16K.wav"
        file_path = os.path.join(audio_path,file_name)
        # print(file_path)
        try:
            song = AudioSegment.from_wav(file_path)
        except Exception as e:
            print(e)
        # song1 = song * 10
        # song1.export(os.path.join(audio_path,'song1.wav'))
        if song.duration_seconds <15:
            result= BAIDU_ASR(file_path,dev_pid)
            with open(os.path.join(result_path,"{}.txt".format(os.path.splitext(file_name)[0])),'a+') as f:
                f.writelines(result)
                f.writelines(os.linesep)
            print(result)
        else:
            #音频总时长
            all_time = song.duration_seconds
            #需要将文件分割的总份数
            cuts = int(math.ceil((all_time / 14 )))
            for i in range(cuts):
                cut_song = song[i*14*1000 : (i+1)*14*1000]
                # print(cut_song.duration_seconds)
                export_file_path = os.path.join(tmp_path,'{}{}.wav'.format(os.path.splitext(file_name)[0],str(i+100)))
                cut_song.export(export_file_path,format="wav",bitrate="16k")
                result = BAIDU_ASR(export_file_path,dev_pid)
                if result is not None:
                    with open(os.path.join(result_path, "{}.txt".format(os.path.splitext(file_name)[0])), 'a+') as f:
                        f.writelines(result)
                        f.writelines(os.linesep)
                        #清除该临时文件
                        os.remove(export_file_path)
                    print(result)

    #清除临时文件
    # for tmp_file in os.listdir(tmp_path):
    #     os.remove(os.path.join(tmp_path,tmp_file))

if __name__ == '__main__':
    #将文件转换为wav文件
    file_2_wav()

    #将wav文件提交到baidu rest api，将文本写入文件
    main_trans(audio_path)

