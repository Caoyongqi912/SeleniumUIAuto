# -*- coding: utf-8 -*-

# @Time    : 2021/8/17 3:07 下午 
# @Author  : cyq
# @File    : seleniumOpt.py
import platform
from selenium.webdriver import ChromeOptions


def options():
    """
    浏览器设置
    :return:
    """
    _options = ChromeOptions()
    # # 设置chrome为手机界面
    # mobileEmulation = Config().get_conf("seleniumOpt", "mobileEmulation")
    # if mobileEmulation == 'true':
    #     mobile_emulation = {"deviceName": "Galaxy S5"}
    #     _options.add_experimental_option("mobileEmulation", mobile_emulation)
    if platform.system() == 'Darwin':
        pass
    else:
        _options.add_argument('--headless')
        _options.add_argument('--no-sandbox')
        _options.add_argument('--disable-gpu')
        _options.add_argument('--disable-dev-shm-usage')

    return _options


def capabilities():
    chrome_capabilities = {
        "browserName": "chrome",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
    }
    return chrome_capabilities

if __name__ == '__main__':
    options()