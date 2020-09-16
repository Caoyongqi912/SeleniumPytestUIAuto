import json
import random
import time

import allure

from Setting.Assert import Assertion
from Setting.Base import PageBase


class CommonMethod(PageBase):
    Assert = Assertion()


    def allure_report(self, func, case_name, piclist, expect=None, res=None):
        allure.dynamic.title(func.__name__)
        allure.dynamic.description(case_name)
        allure.attach(json.dumps(func.__name__, ensure_ascii=False), 'Case_Name',
                      allure.attachment_type.JSON)
        allure.attach(func.__doc__.strip(), 'Step',
                      allure.attachment_type.JSON)
        n = 0
        for i in piclist:
            n += 1
            allure.attach(i, 'Step{}'.format(n), allure.attachment_type.PNG)

        if expect and res:
            allure.attach(json.dumps(expect, ensure_ascii=False), 'expect_response', allure.attachment_type.JSON)
            allure.attach(json.dumps(res, ensure_ascii=False), 'Actual_return', allure.attachment_type.JSON)
        self.log.debug(f"===============  {func.__name__} 测试完成  ===============    \n\n")

    def mouse_to(self):
        """
        鼠标位置归0
        """
        ele = self.find_element(('xpath', "//html"))
        self.ActionChainsOffsetClick(element=ele, x=0, y=0)
        self.log.debug("鼠标归0")
        return ele

    def login(self, user=None, url=None):
        pass
