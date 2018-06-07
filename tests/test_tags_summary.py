#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 15:30
# @Author  : Kaiwen Xue
# @File    : test_tags_summary.py
# @Software: PyCharm
import unittest
from tags_summary import merge_dicts


class TestTagsSummary(unittest.TestCase):

    def test_merge_dicts(self):
        dict_a = {'a': 1, 'b': 2, 'c': 3}
        dict_b = {'a': 2, 'b': 3, 'c': 1}
        dict_c = {'a': 3, 'b': 1, 'c': 2}
        self.assertEqual(merge_dicts(dict_a, dict_b, dict_c), {'a': 6, 'b': 6, 'c': 6})
        self.assertEqual(merge_dicts(dict_a), dict_a)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)