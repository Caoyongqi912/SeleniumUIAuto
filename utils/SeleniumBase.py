# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 2:13 下午 
# @Author  : cyq
# @File    : SeleniumBase.py
import json
import time
import allure
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

from utils.Log import get_log
from utils.Assert import Assert


class SeleniumBaseConfig:
    faker = Faker(locale="zh_CN")
    Assert = Assert
    log = get_log()

    def __init__(self, driver: webdriver):
        """
        :param driver: 驱动
        """
        self.driver = driver

    def find_element(self, locator: tuple, timeout=5):
        """
        find_element
        :param locator: (xpath,xxx）(id,xxx)
        :param timeout: timeout
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            self.log.info(f"[{self.find_element.__name__}]  locator: {locator} element: {str(element)}")
            return element
        except WebDriverException as e:
            self.log.error(e)
            allure.attach(self.get_png(), "异常截图", allure.attachment_type.PNG)
            allure.attach("未找到: {}, 详细信息如下: {}".format(locator, e))
            raise e

    def find_elements(self, locator: tuple, timeout=5) -> [list, WebDriverWait]:
        """
        find_elements
        :param locator:  (xpath,xxx）(id,xxx)
        :param timeout: timeout
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            self.log.info('{} : {}'.format(self.find_element.__name__, elements))
            return elements
        except WebDriverException as e:
            self.log.error(e)
            allure.attach(self.get_png(), "异常截图", allure.attachment_type.PNG)
            allure.attach("未找到: {}, 详细信息如下: {}".format(locator, e))
            raise e

    def click(self, locator: tuple, sleep: int = 1):
        """
        click event
        :param locator: （xpath,xxx）(id,xxx)
        :param sleep:   sleep time
        """
        element = self.find_element(locator)
        try:
            time.sleep(sleep)
            element.click()
        except WebDriverException as e:
            self.log.error(e)
            return

    def get_text(self, locator: tuple, sleep: int = 0) -> [str, None]:
        """
        get_text event
        :param locator: （xpath,xxx）(id,xxx)
        :param sleep:   sleep time
        :return:
        """
        element = self.find_element(locator)
        try:
            time.sleep(sleep)
            text = element.text.strip()
            return text
        except WebDriverException as e:
            self.log.error(e)
            return

    def get_attribute(self, locator: tuple, name: str) -> str:
        """
        get_attribute
        :param locator: （xpath,xxx）(id,xxx)
        :param name:attribute
        :return: attribute
        """
        element = self.find_element(locator)
        try:
            attr = element.get_attribute(name)
            return attr
        except WebDriverException as e:
            self.log.error(e)
            return ""

    def clear(self, locator: tuple):
        """
        clear
        :param locator: （xpath,xxx）(id,xxx)
        :return null
        """
        element = self.find_element(locator)
        try:
            element.send_keys(Keys.CONTROL, "a")
            element.send_keys(Keys.DELETE)
            return
        except WebDriverException as e:
            self.log.error(e)
            return

    def js_clear(self, locator):
        """
        js clear input
        """
        self.click(locator)
        try:
            js = 'document.querySelector("#{}").value="";'.format(locator[1])
            self.driver.execute_script(js)
        except WebDriverException as e:
            self.log.error(e)
            return

    def send_keys(self, locator: tuple, text: str):
        """
        send_keys
        :param locator: （xpath,xxx）(id,xxx)
        :param text: 如参text
        :return:
        """
        element = self.find_element(locator)
        try:
            element.click()
            element.clear()
            element.send_keys(text)
            time.sleep(0.5)
        except WebDriverException as e:
            self.log.error(e)
            return

    def refresh(self):
        """
        refresh
        """
        try:
            self.driver.refresh()
            time.sleep(2)
        except WebDriverException as e:
            self.log.error(e)

    def get_url(self, url: str):
        """
        get_url
        :param url:url
        """
        try:
            self.driver.get(url)
            time.sleep(4)
        except WebDriverException as e:
            self.log.error(e)
            return

    def switch_to_window(self, new_window=None):
        """
        switch_to_window
        :param new_window: 新窗口句柄
        :return: 当前窗口句柄
        """
        if new_window is None:
            current_handle = self.driver.window_handles
            try:
                self.driver.switch_to.window(current_handle[-1])
                return current_handle
            except WebDriverException as e:
                self.log.error(e)
                return
        else:
            self.driver.switch_to.window(new_window)

    def get_png(self):
        """
        get_png
        :return: get_screenshot_as_png
        """
        try:
            return self.driver.get_screenshot_as_png()
        except WebDriverException as e:
            self.log.error(e)

    def go_back(self):
        """
        go_back
        """
        try:
            self.driver.back()
        except WebDriverException as e:
            self.log.error(e)

    def set_browser_size(self):
        """
        set_browser_size
        :return:
        """
        try:
            self.driver.maximize_window()
        except WebDriverException as e:
            self.log.error(e)

    def scroll_into_view(self, locator: tuple):
        """
        scroll_into_view
        """
        element = self.find_element(locator)

        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except WebDriverException as e:
            self.log.error(e)
            return

    def send_script(self, js: str):
        """
        send_script
        :param js: js
        """
        try:
            self.driver.execute_script(js)
        except WebDriverException as e:
            self.log.error(e)
            return

    def action_click(self, locator: tuple):
        """
        action_click
        """
        element = self.find_element(locator)
        try:
            ActionChains(self.driver).move_to_element(element).click().perform()
        except WebDriverException as e:
            self.log.error(e)
            return

    def action_hold(self, locator):
        """
        action_hold
        """
        element = self.find_element(locator)
        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except WebDriverException as e:
            self.log.error(e)
            return

    def action_send_keys(self, locator: tuple, key: str):
        """
        action_send_keys
        """
        element = self.find_element(locator)
        try:
            ActionChains(self.driver).move_to_element(element).click().send_keys(key).perform()
        except WebDriverException as e:
            self.log.error(e)
            return

    def action_offset_click(self, x, y, element=None):
        """
        坐标点击
        :param x:
        :param y:
        :param element:
        :return:
        """
        try:
            if element:
                ActionChains(self.driver).move_to_element_with_offset(element, 0, 0).perform()
            ActionChains(self.driver).move_by_offset(x, y).perform()
        except WebDriverException as e:
            self.log.error(e)
            return

    def mouse_to(self):
        """
        鼠标位置归0
        """
        ele = self.find_element(('xpath', "//html"))
        try:
            self.action_offset_click(element=ele, x=0, y=0)
        except WebDriverException as e:
            self.log.error(e)

    def allure_report(self, func, pics, expect=None, actual=None):
        """
        allure write
        :param func: test_func
        :param pics: get_screenshot_as_pngs
        :param expect: expect value
        :param actual: actual value
        :return:
        """
        allure.attach(json.dumps(func.__name__, ensure_ascii=False), 'Case_Name',
                      allure.attachment_type.JSON)
        if func.__doc__:
            allure.attach(func.__doc__.strip(), 'Step',
                          allure.attachment_type.JSON)

        n = 0

        for i in pics:
            n += 1
            allure.attach(i, 'Step{}'.format(n), allure.attachment_type.PNG)

        if expect and actual:
            allure.attach(json.dumps(expect, ensure_ascii=False), 'Expect ', allure.attachment_type.JSON)
            allure.attach(json.dumps(actual, ensure_ascii=False), 'Actual ', allure.attachment_type.JSON)

        self.log.info("===============  {} 测试完成  ===============    \n".format(func.__name__))

    def quit(self):
        """
        quit
        """
        try:
            self.driver.quit()
        except WebDriverException as e:
            self.log.error(e)
            return

    def get_title(self):
        """
        get_title
        :return: title
        """
        try:
            title = self.driver.title
            return title
        except WebDriverException as e:
            self.log.error(e)
            return

    def scrollIntoView(self, element):
        """
        滚动屏幕到可见
        :param locator: locator
        """
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)  # 拖动到可见的元素去
        except WebDriverException as e:
            self.log.error(e)
            return
