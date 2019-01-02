# -*- coding:utf-8 -*-
_author_ = 'liujihao'

import re


def findJob(text):
    try:
        return re.search('\"职业: (.*)\"', text).group(1)
    except:
        return "none"


def findDegree(text):
    try:
        return re.search('\"等级: (.*)\" ', text).group(1)
    except:
        return "none"


def findCode(text):
    try:
        return re.search('\"存档代码: (.*)\" ', text).group(1)
    except:
        return "none"


def check_valid_path(path):
    try:
        return re.search('(.*)(/TWRPG)$', path)
    except:
        return "none"
