# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2020/4/6 11:22
# @Author  : whd
# @note    : 抓取最好大学网的大学排名; 太麻烦

import requests
from bs4 import BeautifulSoup
import bs4
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent(verify_ssl=False).chrome
}


def gethtml(url):
    try:
        r = requests.get(url, timeout=30, verify=False, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return ''


def processhtml(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody', recursive=True).children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printulist(ulist, num):
    tplt = "{0:<10}\t{1:{4}<10}\t{2:<10}\t{3:<10}"
    print(tplt.format("排名", "学校名称", "总分", "指标得分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))


def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    uinfo = []
    html = gethtml(url)
    processhtml(uinfo, html)
    printulist(uinfo, 20)


if __name__ == '__main__':
    main()
