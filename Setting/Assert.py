# -*- coding: utf-8 -*-
# @Time    : 2019/11/25
# @Author  : caoyongqi
# @File    : Assert.py

from Setting import Log


class Assertion:
    def __init__(self):
        self.log = Log.LogInfo()

    def assert_unequal(self, exp, res):
        try:
            assert exp != res
            return True
        except Exception:
            self.log.error('AssertionError: expect_value is %s, res_val is %s ' % (exp, res))
            raise

    def assert_in(self, res, exp):
        try:
            assert exp in res
            return True
        except Exception:
            self.log.error('AssertionError: expect  is %s, res is %s ' % (exp, res))
            raise

    def assert_equal(self, code, expect_code):
        try:
            assert code == expect_code
            return True
        except Exception:
            self.log.error('AssertionError: expect_value is %s, res_val is %s ' % (expect_code, code))
            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :param comment:
        :return:
        """
        try:
            msg = body[body_msg]

            assert msg == expected_msg
            return True
        except Exception as e:
            self.log.error(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            raise

    def assert_kv(self, response_msg, expect_msg):
        """
        验证response response_msg中是否包含期望返回值key-value是否相等或key存在
        :param response_msg:
        :param expect_msg:
        :return:
        """

        try:
            if isinstance(expect_msg, dict):
                for key in expect_msg.keys():
                    assert key in response_msg
                    if isinstance(expect_msg[key], list):
                        for i in range(len(expect_msg[key])):
                            self.assert_kv(response_msg[key][i], expect_msg[key][i])
                    elif isinstance(expect_msg[key], dict):
                        self.assert_kv(response_msg[key], expect_msg[key])
                    elif expect_msg[key] != '':
                        assert expect_msg[key] == response_msg[key]
            else:
                assert response_msg == expect_msg
            return True
        except Exception:
            self.log.error("AssertionError:\n expect_key   is %s \n responseText is %s" % (expect_msg, response_msg))
            raise

    def assert_value(self, res, exp):
        msg = ''
        try:
            for k, v in res.items():
                if k in exp:
                    msg = k
                    assert res[k] == exp[k]
        except Exception:
            self.log.error(
                "AssertionError:\n %s错误: \n expect_key   is %s \n responseText is %s" % (msg, exp[msg], res[msg]))
            raise

    def assert_list(self, res, exp):
        try:
            for i in exp:
                assert i in res

        except Exception:
            self.log.error(
                "AssertionError:\n 错误: \n expect_key   is %s \n responseText is %s" % (exp, res))
            raise


