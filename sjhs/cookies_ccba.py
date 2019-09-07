#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 10:42
# @Author  : Kaiwen Xue
# @File    : cookies_ccba.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import re
import csv
from time import time


def login_by_post():
    login_url = 'http://ccba6.info/wp-login.php'
    session = requests.session()
    post_data = {'log': 'kaiwen', 'pwd': '**********'}
    session.post(login_url, post_data)
    return session


def find_download_links(session):
    download_list = []
    download_page = 'http://ccba6.info/wp-content/plugins/erphpdown/download.php?postid='
    post_post_page = '&url=&key=1'
    results = {}
    vip_url = 'http://ccba6.info/category/vip'
    r = session.get(vip_url)
    soup = BeautifulSoup(r.text, 'lxml')

    for h2 in soup.find_all('h2'):

        for content in h2.find_all('a'):
            post_number = str(int(re.sub('\D', '', content['href']))-6000000)
            download_list.append(download_page + post_number)

    for download_url in download_list:
        d_page = session.get(download_url)
        soup = BeautifulSoup(d_page.text, 'lxml')
        a = soup.find_all('p')[-1]
        dd = download_url+post_post_page
        results[dd] = a.string

    return results


def csv_generator(results):
    csvfile = open('ccba_download.csv', 'w')
    writer = csv.writer(csvfile)
    writer.writerow(['URL', 'code'])

    for key, value in results.items():
        writer.writerow([key, value])

    csvfile.close()


if __name__ == '__main__':
    print('==============================Script running==============================\n')
    start = time()
    csv_generator(find_download_links(login_by_post()))
    ends = time()
    print('\t\t\t\t\t\t\tRunning time:', str(round(ends - start, 2)) + 's')
    print('\n==================================Result==================================\n')