# -*- coding: utf-8 -*-

# @Time    : 2021/8/17 10:20 上午 
# @Author  : cyq
# @File    : test_register.py

import time
import pytest
import allure
from method.RegisterMthod.registerMethod import RegisterMethod
from config.Config import Config
from config.redisConfig import Redis
from utils.Driver import Driver


@allure.feature("注册测试")
class TestRegister:
    def setup_class(self):
        self.cmURL = Config().get_conf("domain", "cm")
        self.rURL = Config().get_conf("domain", "r")
        self.r = Redis()

    def setup(self):
        self.d = Driver().driver()
        self.driver = RegisterMethod(self.d)
        self.mobile = self.r.get_mobile
        self.two = self.r.get_mobile
        self.driver.get_url(self.rURL)

    def teardown(self):
        self.r.add_mobile(self.mobile)
        self.r.add_mobile(self.two)
        self.driver.quit()

    @pytest.mark.P3
    @allure.title("创建新团队:姓名输入汉字、英文、数字字符")
    @pytest.mark.flaky(reruns=1, reruns_delay=2)
    def test_create_team_username(self):
        """
        姓名输入汉字、英文、数字字符
        1.register
        2.create team
        3.create_team_username
        """
        pics = []
        self.driver.register(self.mobile)
        exp = "true"
        res = self.driver.check_button_disabled()
        self.driver.allure_report(self.test_create_team_username, pics, exp, res)
        self.driver.Assert.assert_equal(exp, res)
