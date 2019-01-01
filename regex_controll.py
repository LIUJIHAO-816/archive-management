# -*- coding:utf-8 -*-
_author_ = 'liujihao'

import re


def findJob(text):
    return re.search('\"职业: (.*)\"', text).group(1)


def findDegree(text):
    return re.search('\"等级: (.*)\" ', text).group(1)


def findCode(text):
    return re.search('\"存档代码: (.*)\" ', text).group(1)


def check_valid_path(path):
    return re.search('(.*)(/TWRPG)$', path)
