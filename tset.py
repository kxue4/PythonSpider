#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 18:55
# @Author  : Kaiwen Xue
# @File    : tset.py
# @Software: PyCharm
import re

data = 'saffe>=sfjwoq啊吧jsis'
a = re.sub(r'[^\u4e00-\u9fa5]', '', data)
print(a)
