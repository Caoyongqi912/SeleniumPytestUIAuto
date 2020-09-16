# -*- coding: utf-8 -*-
# @Author  : caoyongqi
# @File    : main.py

import os
import sys

import pytest

from CaseNum import getNum
from Config.Config import Config
from Setting.Log import LogInfo
from Setting.Shell import Shell

if __name__ == '__main__':
    conf = Config()
    log = LogInfo()
    shell = Shell()
    case_path = 'TestCase'
    ReRunCaseList = ""
    if len(sys.argv) > 2:
        # 自动化执行时，控制台传入报告路径与测试域名
        xml_report_path = os.path.join(sys.argv[1])
        headless = os.path.join(sys.argv[2])
        test_host = os.path.join(sys.argv[3])
        driver = os.path.join(sys.argv[4])
        ReRunCaseList = eval(os.path.join(sys.argv[5]))

        # 初始化config文件
        conf.set_conf('headless', 'headless', headless)
        conf.set_conf('domain', 'domain', test_host)
        conf.set_conf('chromedriver', 'chromedriver', driver)


    else:
        xml_report_path = conf.xml_report_path
    # 获得有所有个case
    caseNum = getNum()[0]
    caseNames = getNum()[1]

    LogInfo.debug(f"<<{str(caseNum)}>>")

    # -n 20 20个进程  -v 详细打印 -case_path 测试地址 -s 关闭捕捉， 输出打印信息 q’:减少测试的运行冗长。
    # -x’:出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。

    args = ["-n 20", "-s", "-v", case_path, '--alluredir', xml_report_path]

    if ReRunCaseList:
        print(ReRunCaseList, '\n')
        ReRunArgs = ["-n 20", "-s", "-v", '--alluredir', xml_report_path]
        for i in ReRunCaseList:
            ReRunArgs.insert(3, i)
        print(ReRunArgs, '\n')

        pytest.main(args=ReRunArgs)
    else:
        pytest.main(args=args)

    # html_report_path = conf.html_report_path
    # if os.path.exists(html_report_path):
    #     shell.invoke('rm -r %s' % html_report_path)
    # cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    # try:
    #     shell.invoke(cmd)
    # except Exception:
    #     log.error('执行用例失败，请检查环境配置')
    #     raise
