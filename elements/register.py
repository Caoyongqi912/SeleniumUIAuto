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


class RegisterCreateTeam(Register):
    # ================== 完善个人信息界面 ================
    INPUT_TYPE = ("xpath", '//input[@placeholder="请选择行业类型"]')
    INPUT_SIZE = ("xpath", '//input[@placeholder="请选择团队规模"]')
    INPUT_CITY = ("xpath", '//input[@placeholder="请选择所在城市"]')

    SELECT_TYPE = ("xpath", "//p[text()='教育']")  # 行业类型选择教育
    SELECT_SIZE = ("xpath", "//p[text()='10人以内']")  # 行业规模选择十人以内
    # 城市选择 北京/直辖市/东城区
    SELECT_CITY = ("xpath", "//span[text()='北京市']")
    SELECT_MUNICIPALITY = ("xpath", "//span[text()='直辖市']")
    SELECT_REGION = ("xpath", "//span[text()='东城区']")

    # ================== 礼包界面 ================
    GET_GIFT_INFO = ("xpath", "//p[@class='get-gift-info-title']")


class RegisterJoinTeam(Register):
    # ================== 加入已有团队 ================
    INPUT_TEAM_CODE = ("xpath", "//input")  # 输入团队吗
    GET_INPUT_ERROR_INFO = ("class", 'default-input-error')  # 获取input 错误信息

    # 已加入
    JOIN_ERROR_INFO = ("xpath", '//p[@class="register-error-modal-info"]')
