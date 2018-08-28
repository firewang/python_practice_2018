raw_file_path  -- 存放原始音视频

audio_files -- 转化后符合转化要求的音频存放处

result -- 输出的 文本文件存放处

tmp_path -- 临时文件存放处, 处理完成后清空

error_info.txt -- 记录错误信息


windows下使用说明：
---第一种方式---
1.依赖于ffmpeg : 下载地址 https://ffmpeg.zeranoe.com/builds/

2.将压缩包解包之后将bin目录的路径添加到系统环境变量path中
    e.g 解压后路径为 D:/ffmpeg
    则将D:/ffmpeg/bin 加入path

3.运行 *.exe 初始化目录

4.将需要提取文本的音视频放入  raw_file_path 文件夹中

5.运行结束后在 result中的同名文件 即为原始音视频的文本内容

---第二种方式---
1.依赖于ffmpeg : 下载地址 https://ffmpeg.zeranoe.com/builds/

2.将压缩包解包之后
   将根目录下文件全部copy到extends目录下
   然后将 ~ /extends/bin 加入系统环境变量中

3.运行 *.exe 初始化目录

4.将需要提取文本的音视频放入  raw_file_path 文件夹中

5.运行结束后在 result中的同名文件 即为原始音视频的文本内容