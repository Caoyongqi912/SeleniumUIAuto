import sys
import time

import pytest
from config.Config import Config
from feishu import fs
from utils.Log import get_log
from config.redisConfig import Redis
log = get_log()

if __name__ == '__main__':
    # 初始化白名单手机号
    Redis().initMobiles()
    conf = Config()
    case_path = 'TestCase'

    xml_report_path = conf.xml_report_path
    if len(sys.argv) > 3:
        runCase = sys.argv[1]  # P1 P2 P3 ALL
        if runCase != "ALL":
            case_path = f"-m={runCase}"
        xml = sys.argv[2]
        if xml:
            xml_report_path = xml
        BUILD_NUMBER = sys.argv[3]
        conf.set_conf("FS", "BUILD_NUMBER", BUILD_NUMBER)

    args = ["-s", "-v", "-n=auto", case_path, '--alluredir', xml_report_path, '--clean-alluredir']

    pytest.main(args=args)
    time.sleep(120)
    fs()

    # -n 20 20个进程  -v 详细打印 -case_path 测试地址 -s 关闭捕捉， 输出打印信息 q’:减少测试的运行冗长。
    # -x’:出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
    # html_report_path = conf.html_report_path
    # if os.path.exists(html_report_path):
    #     shell.invoke('rm -r %s' % html_report_path)
    # cmd = './allure-2.13.6/bin/allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    # shell.invoke(cmd)
    # python3 main.py $level ./allure-results $BUILD_NUMBER
