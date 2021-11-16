# -*- coding: utf-8 -*-

# @Time    : 2021/8/12 6:08 下午 
# @Author  : cyq
# @File    : Shell.py

import subprocess

from utils.Log import get_log

log = get_log()


class Shell:

    @staticmethod
    def invoke(cmd):
        log.info("cmd = [{}]".format(cmd))
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        e = errors.decode("utf-8")
        if o:
            log.info(f"o:{o}")
            return o
        elif e:
            log.error(f"e:{e}")
            return e
