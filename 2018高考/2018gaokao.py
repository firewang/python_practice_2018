# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/6/10 22:23
# @Author  :  wanghuodong  
# @note

import pyecharts as pe
import pandas as pd


data =  pd.read_excel("./data_gaokao/data_gaokao.xlsx",).sort_values(by='年份',ascending=True)
gaokao_years = list(data["年份"].values)
gaokao_populations = [x.split("万")[0] for  x in data['高考人数'].values]
gaokao_luqu = [x.split("万")[0] for  x in data["录取人数"].values]
gaokao_luqulv = list( data[ "录取率"].values)

#初始化页面
page = pe.Page("高考可视化")


bar = pe.Bar("1977-2018历年高考报名人数与录取人数",
             subtitle="Source:http://edu.sina.com.cn/zt_d/gkbm/",
             title_pos = 'center',)
bar.add("报名人数",gaokao_years,gaokao_populations)
bar.add("录取人数",gaokao_years,gaokao_luqu,
        yaxis_name = '万人/年',
        yaxis_name_gap= 50,
        legend_top='bottom',
        xaxis_rotate=30,
        xaxis_interval=0,
        is_datazoom_show=True,datazoom_range=[0,25]
        )
page.add(bar)

line = pe.Line("1977-2017历年高考录取率",
               subtitle="Source:http://edu.sina.com.cn/zt_d/gkbm/",
             title_pos = 'center',)
line.add("录取率",
         gaokao_years,
         gaokao_luqulv,
         legend_top='bottom',
         is_label_show=True,
         xaxis_rotate=30,
         xaxis_interval=0,
         is_datazoom_show=True,datazoom_range=[0,25]
         )
page.add(line)




page.render("./高考.html")