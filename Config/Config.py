# -*- coding: utf-8 -*-
# @Author  : caoyongqi
# @File    : Config.py

import os
from configparser import ConfigParser

from importlib_metadata import FileNotFoundError

class Config:
    # path
    path = os.path.dirname(os.path.dirname(__file__))

    def __init__(self):
        self.xml_report_path = Config.path + '/report/DispatchXml'
        self.html_report_path = Config.path + '/report/DispatchHtml'
        self.pic_path = Config.path + '/report/Pic'

        self.config = ConfigParser()
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

        if not os.path.exists(self.config_path):
            raise FileNotFoundError('配置文件不存在！')

        self.config.read(self.config_path)

        # domain
        self.domain = self.get_conf('domain', 'domain')

        # login
        self.username = self.get_conf('username', 'username')
        self.password = self.get_conf('password', 'password')

    def get_conf(self, title, value):
        """
        read .ini
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        change .ini
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.config_path, 'w+') as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        add .ini
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.config_path, 'w+') as f:
            return self.config.write(f)
