# -*- coding: utf-8 -*-

# @Time    : 2021/8/17 3:12 下午 
# @Author  : cyq
# @File    : Request.py

import requests
import requests.adapters as ad

from utils.Log import get_log

log = get_log()


class Request:
    def __init__(self):
        ad.DEFAULT_RETRIES = 5
        self.headers = {
            "Content-Type": "application/json"
        }

    def requests(self, method, host, url, data):

        if method == 'POST':
            self.response = requests.post(url=host + url, json=data, headers=self.headers)
            print(self.response.json())
        elif method == "GET":
            self.response = requests.get(url=host + url, params=data)
            print(self.response.json())



if __name__ == '__main__':
    data = {"productID":7}
    a ={'status': 'success',
     'data': '{"title":"","sessionName":"zentaosid","sessionID":"3l9jdj48gugth2sf26v3b42tet","rand":5612,"pager":null}',
     'md5': '2c480c58c84107d1a988d174bb217e6d'}

    Request().requests(method="GET",host="http://zentao.duobeiyun.com:82/index.php?t=json",url="",data=data)