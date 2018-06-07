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
        self.assertEqual(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'a': 2, 'b': 3, 'c': 1}, {'a': 3, 'b': 1, 'c': 2}), {'a': 6, 'b': 6, 'c': 6})


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)