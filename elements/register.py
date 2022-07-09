# -*- coding: utf-8 -*-

# @Time    : 2021/8/17 10:15 上午 
# @Author  : cyq
# @File    : register.py

class Register:
    # ================== 公共 ================
    # 下一步
    NEXT_STEP_BUTTON = ("xpath", "//button")
    # 返回
    RETURN = ('xpath', '//p[@class="return-prev-step"]')
    # input 错误信息
    INPUT_ERROR_INFO = ("xpath", '//p[@class="default-input-error"]')

    # ================== home界面 ================
    CREATE_BUTTON = ("xpath", "//div[text()='创建']")  # 创建button
    JOIN_BUTTON = ("xpath", "//div[text()='加入']")  # 创建button

    INPUT_TEAM_NAME = ("xpath", '//input[@placeholder="请输入团队名称"]')  # 输入团队名称
    INPUT_YOUR_NAME = ("xpath", '//input[@placeholder="请输入你的姓名"]')  # 输入个人名称


class RegisterLogin(Register):
    # ================== 登录界面 ================
    INPUT_NUMBER = ("xpath", "//input")

    # ================== 录入code ================
    SEND_CODE_0 = ("xpath", "//div[1]/input")
    SEND_CODE_1 = ("xpath", "//div[2]/input")
    SEND_CODE_2 = ("xpath", "//div[3]/input")
    SEND_CODE_3 = ("xpath", "//div[4]/input")

    # 获取验证码信息
    MSG = ('xpath', '//div[contains(@class,"toast__text")]')
    # 重新获取验证码
    REACQUIRE_CODE_BUTTON = ('xpath', '//p[text()="重新获取验证码"]')
    # 验证已发送
    MOBILE_DESC = ("xpath", '//p[@class="check-mobile-desc"]')
    # 验证码错误文本
    INVALID_COD_MSG = ("xpath", "//div[contains(@class,'error_con')]/p")

