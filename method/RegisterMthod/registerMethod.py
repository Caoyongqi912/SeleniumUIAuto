# -*- coding: utf-8 -*-

# @Time    : 2021/8/17 10:30 上午 
# @Author  : cyq
# @File    : registerMethod.py
import time

from utils.Log import ilog
from utils.SeleniumBase import SeleniumBaseConfig
from elements.register import Register, RegisterLogin, RegisterCreateTeam, RegisterJoinTeam


class RegisterMethod(SeleniumBaseConfig):


    def __init__(self, driver):
        super().__init__(driver)

    def register(self, mobile: str):
        """
        注册
        :param mobile
        :return:
        """
        self.send_keys(RegisterLogin.INPUT_NUMBER, mobile)
        self.click(RegisterLogin.NEXT_STEP_BUTTON)
        time.sleep(1)

    def input_code(self, code: list[str] = None):
        """
        录入验证码
        下一步
        :param code [1,2,3,4]
        """

        if code:
            self.send_keys(RegisterLogin.SEND_CODE_0, code[0])
            self.send_keys(RegisterLogin.SEND_CODE_1, code[1])
            self.send_keys(RegisterLogin.SEND_CODE_2, code[2])
            self.send_keys(RegisterLogin.SEND_CODE_3, code[3])
        else:
            self.send_keys(RegisterLogin.SEND_CODE_0, "1")
            self.send_keys(RegisterLogin.SEND_CODE_1, "2")
            self.send_keys(RegisterLogin.SEND_CODE_2, "3")
            self.send_keys(RegisterLogin.SEND_CODE_3, "4")
        self.click(RegisterLogin.NEXT_STEP_BUTTON)

