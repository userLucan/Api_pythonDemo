#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-04 15:09
# @Author  : 刘开
# 实时分析



import requests
import pytest

from commen.global_variable import TestGlobal
import allure


class TestAnalysis():
    @classmethod
    def setup_class(self):
        self.config1 = TestGlobal()

    @classmethod
    def teardown(cls):
        print('执行完毕')

    def test_00(self):
        """校验产品线"""
        url = '/crystalBall-web/orgLine/getLines?userId=8D3BEF1526A2DBE1E0530100007F1F9E&token=' + self.config1.get_token()
        response = requests.get(url=self.config1.test_url() + url)
        assert len(response.json()['data']) >= 1

    def test_01(self):
        """校验非凡云高清查询所有"""
        url = '/crystalBall-web/overall/realByMin?line=3&region=10&token=' + self.config1.get_token()
        response = requests.get(url=self.config1.test_url() + url)
        assert len(response.json()['data']) >= 1

    def test_02(self):
        """校验4k查询杭州地区"""
        url = '/crystalBall-web/overall/realByMin?line=17&region=1001&token=' + self.config1.get_token()
        response = requests.get(url=self.config1.test_url() + url)
        assert len(response.json()['data']) >= 1


if __name__ == '__main__':
    pytest.main()
