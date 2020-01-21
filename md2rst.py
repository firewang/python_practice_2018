# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2020/1/21 16:53
# @Author  : wanghd
# @note    : 

import requests


def md_to_rst(from_file, to_file):
    """
    将markdown格式转换为rst格式
    @param from_file: {str} markdown文件的路径
    @param to_file: {str} rst文件的路径
    """
    response = requests.post(
        url='http://c.docverter.com/convert',
        data={'to': 'rst', 'from': 'markdown'},
        files={'input_files[]': open(from_file, 'rb')}
    )

    if response.ok:
        with open(to_file, "wb") as f:
            f.write(response.content)


if __name__ == '__main__':
    md_to_rst("readthedocs.md", "read.rst")
