#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
说明: 环境变量`KJWJ_UP`账号和密码用`-`分割     例如： 账号-密码
cron: 20 12 * * *
new Env('科技玩家-签到');
"""
import os, sys
import json

try:
    import requests
except Exception as e:
    print(e, "\n缺少requests 模块，请在青龙后台-依赖管理-Python3 搜索安装")
    exit(3)

try:
    import aiohttp
except Exception as e:
    print(e, "\n缺少aiohttp 模块，请在青龙后台-依赖管理-Python3 搜索安装")
    exit(3)

try:
    import asyncio
except Exception as e:
    print(e, "\n缺少asyncio 模块，请在青龙后台-依赖管理-Python3 搜索安装")
    exit(3)

try:
    import random
except Exception as e:
    print(e, "\n缺少random 模块，请在青龙后台-依赖管理-Python3 搜索安装")
    exit(3)

################################ 【Main】################################
pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
UserAgent = ''


## 获取通知服务
class msg(object):
    def __init__(self, m):
        self.str_msg = m
        self.message()

    def message(self):
        global msg_info
        print(self.str_msg)
        try:
            msg_info = "{}\n{}".format(msg_info, self.str_msg
