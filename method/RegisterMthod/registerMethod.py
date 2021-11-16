# -*- coding: utf-8 -*-

# @Time    : 2021/8/17 10:30 上午 
# @Author  : cyq
# @File    : registerMethod.py
import time

from utils.Log import ilog
from utils.SeleniumBase import SeleniumBaseConfig
from elements.register import Register, RegisterLogin, RegisterCreateTeam, RegisterJoinTeam


class RegisterMethod(SeleniumBaseConfig):
    NEXT_STEP_BUTTON = Register.NEXT_STEP_BUTTON
    RETURN = Register.RETURN

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

    def do(self, mobile, teamName, userName):
        """
        注册一个新公司
        :return: pic
        """
        self.register(mobile)
        self.input_code()
        self.create_team(teamName, userName)
        pic = self.get_png()
        self.click(Register.NEXT_STEP_BUTTON)
        return pic

    def click_resend_mobile_button(self):
        """
        点击重新获取验证码
        :return: pic
        """
        self.click(RegisterLogin.REACQUIRE_CODE_BUTTON)
        return self.get_png()

    def get_send_mobile_desc(self):
        """
        验证手机号
        :return:  请输入发送至 +8618888888888 的4位验证码，有效期10分钟；如未收到，请尝试重新获取验证码。
        """
        return self.get_text(RegisterLogin.MOBILE_DESC)

    def get_resend_mobile_msg(self):
        """
        点击重新获取验证码信息
        :return: text
        """
        text = self.get_text(RegisterLogin.MSG)
        return text

    def get_invalid_code_msg(self):
        """
        验证错误
        :return: text
        """
        return self.get_text(RegisterLogin.INVALID_COD_MSG)

    def get_input_error_info(self):
        """
        获取input 标签错误信息
        :return ：text
        """
        eles  =self.find_elements(Register.INPUT_ERROR_INFO)
        for i in eles:
            text = i.text.strip()
            if text:
                return text



    def get_register_maxlength(self):
        """
        获取 input 标可输入最长
        :return: length
        """
        length = self.get_attribute(RegisterLogin.INPUT_NUMBER, "maxlength")
        return length

    def check_button_disabled(self):
        """
        检查下一步按钮是否可以点击
        :return: disabled or ""
        """
        disable = self.get_attribute(RegisterLogin.NEXT_STEP_BUTTON, "disabled")
        return disable

    def get_gift_info(self):
        """
        获取礼物信息
        :return:  text
        """
        text = self.get_text(RegisterCreateTeam.GET_GIFT_INFO)
        return text

    def get_join_error_info(self):
        """
        获取已加入信息
        :return: text
        """
        text = self.get_text(RegisterJoinTeam.JOIN_ERROR_INFO)
        return text

    # create team
    def click_create_team_button(self):
        """
        点击创建团队

        """
        self.click(RegisterCreateTeam.CREATE_BUTTON)

    def get_input_teamName_maxlength(self):
        """
        获得团队名长度
        :return: length
        """
        length = self.get_attribute(RegisterCreateTeam.INPUT_TEAM_NAME, "maxlength")
        return length

    def create_team_input_teamName(self, teamName):
        """
        创建团队
        :param teamName:
        """
        self.send_keys(RegisterCreateTeam.INPUT_TEAM_NAME, teamName)

    def create_team_input_userName(self, userName):
        """
        创建团队
        :param userName:
        """
        self.send_keys(RegisterCreateTeam.INPUT_YOUR_NAME, userName)

    def input_team_info(self):
        """
        完善用户信息—
        :return:  pic
        """
        self.click(RegisterCreateTeam.INPUT_TYPE)
        self.click(RegisterCreateTeam.SELECT_TYPE)
        self.click(RegisterCreateTeam.INPUT_SIZE)
        self.click(RegisterCreateTeam.SELECT_SIZE)
        self.click(RegisterCreateTeam.INPUT_CITY)
        time.sleep(1)
        self.click(RegisterCreateTeam.SELECT_CITY)
        self.click(RegisterCreateTeam.SELECT_MUNICIPALITY)
        self.click(RegisterCreateTeam.SELECT_REGION)
        pic = self.get_png()
        self.click(RegisterCreateTeam.NEXT_STEP_BUTTON)
        return pic

    def create_team(self, teamName, userName):
        """
        创建团队
        领取礼包
        :param userName: 姓名
        :param teamName: 团队
        :return: pic
        """
        pics = []
        self.click_create_team_button()
        self.create_team_input_teamName(teamName)
        self.create_team_input_userName(userName)

        pics.append(self.get_png())
        self.click(RegisterCreateTeam.NEXT_STEP_BUTTON)
        # 完善用户信息
        pics.append(self.input_team_info())
        self.click(RegisterCreateTeam.NEXT_STEP_BUTTON)
        return pics

    # join

    def click_join_team(self):
        """
        点击加入
        :return:
        """
        self.click(RegisterJoinTeam.JOIN_BUTTON)

    def input_team_code(self, code: str):
        """
        input_team_code
        :param code:  code
        :return:
        """

        self.click(RegisterJoinTeam.INPUT_TEAM_CODE)
        self.send_keys(RegisterJoinTeam.INPUT_TEAM_CODE, code)

    def input_name(self, name):
        """join 录入姓名"""
        self.click(RegisterJoinTeam.INPUT_YOUR_NAME)
        self.send_keys(RegisterJoinTeam.INPUT_YOUR_NAME, name)

    def join(self, code: str, name: str):
        """
        加入团队
        :param code: 团队代码
        :param name: 用户名
        :return:pic;
        """
        self.click_join_team()
        self.input_team_code(code)
        self.click(RegisterJoinTeam.NEXT_STEP_BUTTON)
        self.input_name(name)
        self.click(RegisterJoinTeam.NEXT_STEP_BUTTON)
        return self.get_png()
