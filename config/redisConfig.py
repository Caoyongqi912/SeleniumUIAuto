# -*- coding: utf-8 -*-

# @Time    : 2021/9/3 5:47 下午 
# @Author  : cyq
# @File    : redisConfig.py


import redis
from config.Mobiles import Mobiles


class Redis:

    def __init__(self, host='192.168.0.66', port=6379, password="123456"):
        self.r = redis.Redis(host=host, port=port, password=password)

    def initMobiles(self):
        """
        初始化白名单手机号
        :return:
        """
        if self.r.exists("mobiles"):
            self.r.delete("mobiles")
        for i in Mobiles().l:
            self.r.lpush("mobiles", i)

    def check_mobile(self):
        print(self.r.lrange("mobiles",1,80))

    @property
    def get_mobile(self):
        m = self.r.rpop("mobiles")
        return m.decode('utf-8')

    def add_mobile(self, mobile: str):
        self.r.lpush("mobiles", mobile)

if __name__ == '__main__':
    r = Redis()
    r.check_mobile()