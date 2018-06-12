#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 16:15
# @Author  : Kaiwen Xue
# @File    : my_wp.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import re


url = 'http://kevinbot.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

for content in soup.findAll('p', class_='site-description'):
    print(content.string)

a = soup.findAll('a', rel='bookmark')
print('------find_the_link_of_article------')
for content in a:
    print(content['href'])