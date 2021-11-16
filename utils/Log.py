# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 3:28 下午 
# @Author  : cyq
# @File    : Log.py


import logging
import os
import time


def get_cwd():
    path = os.path.split(os.path.dirname(__file__))[0]
    # 当前文件的绝对路径
    return path


def get_log():
    # 获取项目的根目录
    project_path = get_cwd()
    Logs_path = os.path.join(project_path, 'logs')
    # 获取本地时间，转为年-月-日格式
    local_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 日期文件夹路径
    date_file_path = os.path.join(Logs_path, local_date)
    # 如果没有日期文件夹，创建该文件夹
    if not os.path.exists(date_file_path):
        os.makedirs(date_file_path)
    # 完整日志存放路径
    all_log_path = os.path.join(date_file_path, 'All_Logs/')
    # 如果没有完整日志文件夹，创建该文件夹
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)
    # 错误日志存放路径
    error_log_path = os.path.join(date_file_path, 'Error_Logs/')
    # 如果没有错误日志文件夹，创建该文件夹
    if not os.path.exists(error_log_path):
        os.makedirs(error_log_path)

    # 获取本地时间，转为年月日时分秒格式
    local_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # 设置日志文件名
    all_log_name = all_log_path + local_time + '.log'
    error_log_name = error_log_path + local_time + '.log'

    # 创建一个logger
    logger = logging.getLogger()
    logger.handlers.clear()

    # 创建一个handler写入所有日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)

    # 创建一个handler写入错误日志
    eh = logging.FileHandler(error_log_name)
    eh.setLevel(logging.ERROR)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('[%(asctime)s  - %(levelname)s] - %(message)s')
    # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
    error_log_formatter = logging.Formatter(
        '[%(asctime)s  - %(levelname)s - %(module)s  - %(lineno)s] - %(message)s')

    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    eh.setFormatter(error_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(eh)
    return logger


def ilog(func):
    log = get_log()

    def wrapper(*args, **kwargs):
        doc = ""
        if func.__doc__:
            doc = func.__doc__.strip().split(":")[0].strip()
        log.info(
            "{} >> {} >>  params: {} {}".format(func.__name__,
                                                doc,
                                                args,
                                                kwargs))
        func(*args, **kwargs)

    return wrapper
