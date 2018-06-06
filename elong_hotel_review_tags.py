#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 13:44
# @Author  : Kaiwen Xue
# @File    : elong_hotel_review_tags.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import re
import datetime


pre_url = "http://hotel.elong.com/00"
m = 101000
n = 1
post_url = "/#review"
tag_pattern = "<span>(.*)</span>"
start = datetime.datetime.now()
total_hotel = 0
results = {}

while n < 1001:
    url = pre_url + str(m + n) + post_url
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    tag_raw =soup.find_all('li', method = "filterCommentByTag")

    if tag_raw:

        for elements in tag_raw:
            tag = str(elements).split('\t')[-1].split('<span>')[0]
            count = re.findall(tag_pattern, str(elements).split('\t')[-1])[0]
            results[tag] = int(count) + results.get(tag, 0)

        total_hotel += 1

    n += 1

end = datetime.datetime.now()
print(results)
print('Total hotel numbers:', total_hotel, '\nRunning time:', end-start)


# 30101000 138家: r_1 = {'出行方便': 6593, '性价比高': 17355, '去机场方便': 32, '服务周到': 3079, '设施齐全': 6075, '位置优越': 3033, '离地铁站近': 6714, '前台热情': 1078, '服务态度好': 1472, '贴心服务': 199, '价格实惠': 1519, '餐饮不错': 1018, '环境优雅': 900, '床品舒适': 301, '老板热情': 70, '交通便利': 10223, '大堂气派': 100, '吃饭方便': 3640, '地理位置好': 2193, '离商业街近': 267, '在市中心': 503, '离展馆近': 46, '购物方便': 1323, '离火车站近': 1274, '逛街方便': 102, '离景点近': 307, '吃喝玩乐方便': 24, '离步行街近': 47, '夜景美': 29, '设施设备好': 44, '离车站近': 126, '离市区近': 96, '离码头近': 17, '风景优美': 9, '有历史感': 41, '离汽车站近': 27, '离南站近': 41, '离高铁站近': 28, '古色古香': 61, '离小吃街近': 12, '转机方便': 5, '私密性好': 120, '接送机方便': 190, '温泉不错': 776, '人文特色': 5, '适合度假': 28, '空气清新': 28}
# 00501000 149家: r_2 = {'性价比高': 7290, '出行方便': 6880, '服务周到': 2760, '交通便利': 5483, '价格实惠': 1442, '设施齐全': 2684, '前台热情': 1719, '服务态度好': 1190, '吃饭方便': 2155, '地理位置好': 681, '购物方便': 1207, '位置优越': 637, '离火车站近': 1577, '床品舒适': 129, '离商业街近': 118, '离车站近': 161, '离高铁站近': 15, '在市中心': 153, '环境优雅': 416, '老板热情': 91, '吃喝玩乐方便': 62, '离地铁站近': 1029, '逛街方便': 46, '贴心服务': 55, '空气清新': 11, '离北站近': 55, '离市区近': 28, '餐饮不错': 76, '古色古香': 18, '离景点近': 42, '设施设备好': 3, '离汽车站近': 49, '离展馆近': 5, '去机场方便': 11, '离海边近': 182, '有私人海滩': 10, '卫浴干净': 3, '温泉不错': 5, '离高铁近': 6, '离夜市近': 7}
# 00501300 59家: r_3 = {'购物方便': 299, '出行方便': 1330, '交通便利': 863, '性价比高': 1603, '设施齐全': 737, '前台热情': 383, '服务周到': 665, '吃饭方便': 577, '价格实惠': 304, '地理位置好': 112, '服务态度好': 258, '离火车站近': 465, '离车站近': 53, '位置优越': 128, '老板热情': 98, '在市中心': 27, '贴心服务': 40, '环境优雅': 72, '床品舒适': 18, '离高铁站近': 26, '离商业街近': 14, '离高铁近': 3, '离市区近': 9, '吃喝玩乐方便': 23, '餐饮不错': 28, '逛街方便': 3, '空气清新': 5, '离景点近': 7, '离地铁站近': 10, '去机场方便': 6, '接送机方便': 3, '离汽车站近': 5}
# 00101000 128家: r_4 = {'出行方便': 13621, '离地铁站近': 7401, '离景点近': 461, '性价比高': 11164, '交通便利': 8170, '吃饭方便': 4153, '服务周到': 3802, '设施齐全': 4275, '服务态度好': 1500, '价格实惠': 1483, '地理位置好': 1679, '位置优越': 2235, '购物方便': 1645, '在市中心': 337, '餐饮不错': 315, '环境优雅': 348, '离南站近': 9, '离商业街近': 113, '离火车站近': 171, '前台热情': 2646, '贴心服务': 98, '去机场方便': 57, '离市区近': 74, '老板热情': 228, '大堂气派': 13, '设计有特色': 17, '逛街方便': 35, '接送机方便': 135, '转机方便': 44, '离城墙近': 20, '床品舒适': 153, '离车站近': 84, '离小吃街近': 39, '离高铁站近': 9, '夜景美': 6, '离展馆近': 44, '离步行街近': 69, '吃喝玩乐方便': 36, '设施设备好': 33, '离汽车站近': 37, '空气清新': 28, '私密性好': 83, '离东站近': 4, '温泉不错': 256, '适合度假': 3, '古色古香': 8}
# 92771000 40家: r_5 = {'老板热情': 275, '离小吃街近': 3, '在市中心': 23, '吃喝玩乐方便': 4, '交通便利': 219, '性价比高': 335, '出行方便': 274, '吃饭方便': 84, '设施齐全': 338, '购物方便': 70, '位置优越': 75, '价格实惠': 57, '前台热情': 123, '地理位置好': 73, '离地铁站近': 17, '服务态度好': 149, '离南站近': 7, '服务周到': 260, '环境优雅': 19, '空气清新': 18, '离商业街近': 3, '床品舒适': 26, '贴心服务': 44, '离景点近': 8, '风景优美': 15, '依山傍水': 3, '夜景美': 12, '设施设备好': 4, '离海边近': 7, '无敌海景': 4, '接送机方便': 3, '离码头近': 10, '湖景美': 17, '离车站近': 7}
# 00101000 578家: r_6 = {'出行方便': 38463, '离地铁站近': 18782, '离景点近': 1084, '性价比高': 34207, '交通便利': 23007, '吃饭方便': 13181, '服务周到': 14957, '设施齐全': 14221, '服务态度好': 5148, '价格实惠': 5493, '地理位置好': 5196, '位置优越': 4948, '购物方便': 4162, '在市中心': 808, '餐饮不错': 786, '环境优雅': 1131, '离南站近': 30, '离商业街近': 310, '离火车站近': 1287, '前台热情': 8662, '贴心服务': 416, '去机场方便': 146, '离市区近': 155, '老板热情': 2204, '大堂气派': 21, '设计有特色': 50, '逛街方便': 139, '接送机方便': 319, '转机方便': 90, '离城墙近': 20, '床品舒适': 464, '离车站近': 203, '离小吃街近': 159, '离高铁站近': 22, '夜景美': 6, '离展馆近': 58, '离步行街近': 88, '吃喝玩乐方便': 84, '设施设备好': 87, '离汽车站近': 124, '空气清新': 126, '私密性好': 112, '离东站近': 4, '温泉不错': 271, '适合度假': 7, '古色古香': 70, '离美食街近': 7, '卫浴干净': 39, '离海边近': 10, '离夜市近': 6, '离高铁近': 3, '有历史感': 5, '民俗特色': 3, '离古城近': 3}