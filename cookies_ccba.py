#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 10:42
# @Author  : Kaiwen Xue
# @File    : cookies_ccba.py
# @Software: PyCharm
import requests


def login_by_post():
    url = 'http://ccba6.info/wp-login.php'
    session = requests.session()
    post_data = {'log': 'kaiwen', 'pwd': '**********'}
    session.post(url, post_data)
