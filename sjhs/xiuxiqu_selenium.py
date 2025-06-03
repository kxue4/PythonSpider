#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 14:42
# @Author  : Kaiwen Xue
# @File    : xiuxiqu_selenium.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import time
import requests


def get_soup(url):
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

# session登录 需要cookie
# 获取每页文章的Title和网址
# page_url = 'http://xiuxiqu.wtf/page/1'
# response = session.get(page_url, headers=headers)
# soup = BeautifulSoup(response.text, 'lxml')
# a = soup.find(class_='post-list group').find_all('a', rel='bookmark')
# for i in a:
#     print(i['title'], i['href'])

# 下载 article_soup


def article_page():
    article_soup = get_soup('https://xiuxiqu.wtf/sj/29409')

    # 判断vip下载还是免费下载，处理后返回EHT网盘链接
    if article_soup.find(class_='down-tip'):
        EHT_link = article_soup.find(class_='down-tip').find('a')['href']
    else:
        EHT_link = article_soup.find(class_='download_link')['href']

    if 'url' in EHT_link:
        EHT_link = EHT_link
    else:
        EHT_link = EHT_link + '&url=&key=1'

    EHT_soup = get_soup(EHT_link)
    print(EHT_soup)


if __name__ == '__main__':
    cookie = 'xmicrox%7C1569062077%7C8UHY1yfLvfb43DfSeyD1znzB90ioz3GOxyiIqvqvRwe%7Cca620215ed694e93b7d22d5fbf45978f3649d0b3108e0a7077ca60d246a5e5b5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': cookie,
    }
    url = 'https://xiuxiqu.wtf/user/login?redirect_to=https%3A%2F%2Fxiuxiqu.wtf%2F'
    session = requests.Session()

    print(get_soup('https://www.xiuxiqu.wtf'))
    # article_page()