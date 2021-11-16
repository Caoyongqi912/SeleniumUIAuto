# -*- coding: utf-8 -*-

# @Time    : 2021/8/25 8:31 下午 
# @Author  : cyq
# @File    : Driver.py
import os

from config.Config import Config
from selenium import webdriver
import platform
from utils.seleniumOpt import capabilities, options
from webdriver_manager.chrome import ChromeDriverManager
from utils.Log import get_log

log = get_log()


class Driver:

    @classmethod
    def driver(cls):
        try:
            # select local or docker
            # if platform == "Darwin":
            # url = Config().get_conf("dockerHub", "url")
            # driver = webdriver.Remote(url, desired_capabilities=capabilities(),
            #                           options=options())
            # # else:
            if platform.system() == "Linux":
                executable_path = os.path.join(os.path.dirname(__file__), "chromedriver")
                driver = webdriver.Chrome(executable_path=executable_path, options=options())
            else:
                executable_path = ChromeDriverManager().install()
                driver = webdriver.Chrome(executable_path=executable_path, options=options())
            driver.implicitly_wait(20)
            log.info(f"driver:{driver.name}")
            return driver
        except BaseException as e:
            log.error(e)
            raise e
