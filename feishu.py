# -*- coding: utf-8 -*-

# @Time    : 2021/8/30 10:14 上午 
# @Author  : cyq
# @File    : feishu.py
from config.Config import Config
from utils.Request import Request


def fs():
    BUILD_NUMBER = Config().get_conf("FS", 'BUILD_NUMBER')
    body = {"msg_type": "text", "content": {
        "text": "hi all \ntosee auto build success ! \ncheck detail: http://192.168.0.66:8080/job/ToseeAuto/{}/allure/".format(
            BUILD_NUMBER)}}
    Request().requests(method='POST', host="https://open.feishu.cn",
                       url='/open-apis/bot/v2/hook/xxx',
                       data=body)

if __name__ == '__main__':
    fs()
