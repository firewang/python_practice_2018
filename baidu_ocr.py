# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2020/9/28 10:15
# @Author  :  firewang  
# @note    : 调用百度AI 文字识别接口， 识别图片文字

import json
import requests
import base64


def get_words(fig_path, ocr_type="general"):
    """
    :param fig_path: 图片路径
    :param ocr_type: general 标准含位置版 500次， general_basic 50000次
    :return:
    """
    request_url = f"https://aip.baidubce.com/rest/2.0/ocr/v1/{ocr_type}"
    # 二进制方式打开图片文件
    f = open(fig_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=o5h0WAUse6ka5Y8xgV2WcGOA&client_secret=ScGdml5cwKwkaxK1KEDztY7plbFups18'
    response = requests.get(host)  # 获取access_token
    if response:
        res = response.json()
        access_token = res["access_token"]
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            ocr_result = response.json()
            print(json.dumps(ocr_result, indent=4, ensure_ascii=False))
            words_result = "".join([words["words"] for words in ocr_result["words_result"]])
            print(words_result)
            return words_result
    else:
        return None


if __name__ == "__main__":
    get_words(r"Snipaste_2020-09-28_15-54-01.png", 'general_basic')
