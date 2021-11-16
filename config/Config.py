# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 4:18 下午 
# @Author  : cyq
# @File    : Config.py
import os
from configparser import ConfigParser
from utils.Log import get_log
from queue import Queue

log = get_log()


class Config:
    # path
    path = os.path.dirname(os.path.dirname(__file__))

    def __init__(self):
        self.xml_report_path = Config.path + '/report/DispatchXml'
        self.html_report_path = Config.path + '/report/DispatchHtml'
        self.pic_path = Config.path + '/report/Pic'

        self.config = ConfigParser()
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

        if not os.path.exists(self.config_path):
            raise FileNotFoundError('配置文件不存在！')
        self.config.read(self.config_path)

    def get_mobile(self):
        mobiles = [i.strip() for i in self.config.get("mobiles", "mobile").split(",")]

        try:
            print(len(mobiles))
            first_value = mobiles.pop(0)
            self.set_conf("mobiles", "mobile", ",".join(mobiles))
            return first_value
        except:
            pass
        finally:
            self.set_conf("mobiles", "mobile", ",".join(mobiles))


    def add_mobile(self, mobile):
        mobiles = [i.strip() for i in self.config.get("mobiles", "mobile").split(",")]
        mobiles.append(mobile)
        self.config.set("mobiles", "mobile", ",".join(mobiles))
        with open(self.config_path, 'w+') as f:
            return self.config.write(f)

    def get_conf(self, title, value):
        """
        read .ini
        :param title:
        :param value:
        :return:
        """
        log.info("{} : {}:{}".format(self.get_conf.__name__, title, value))
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        change .ini
        :param title:
        :param value:
        :param text:
        :return:
        """

        log.info("{} : {}:{}:{}".format(self.set_conf.__name__, title, value, text))

        self.config.set(title, value, text)
        with open(self.config_path, 'w+') as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        add .ini
        :param title:
        :return:
        """

        log.info("{} : {}".format(self.add_conf.__name__, title))

        self.config.add_section(title)
        with open(self.config_path, 'w+') as f:
            return self.config.write(f)


if __name__ == '__main__':
    a = Config().get_mobile()
    Config().add_mobile(a)