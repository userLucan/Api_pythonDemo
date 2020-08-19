#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-06 16:57
# @Author  : 刘开

import requests
import pytest
from commen.config import Config


class TestAnalysis():
    @classmethod
    def setup_class(cls):
        cls.config = Config()

    @classmethod
    def teardown(cls):
        print('执行完毕')

    def test_01(self):
        """校验数据列表"""
        url = '/crystalBall-web/user/UserTrends'
        data={
            "cycle_id": 202004,
            "line": 3,
            "region": 10,
            "token":self.config.get_value('cookie.conf','token', 'token')
        }
        response = requests.post(url=self.config.get_value('host.conf', 'host', 'url') + url,data=data)
        assert len(response.json()['data']) >= 1

    def test_02(self):
        """校验用户流向"""
        url = '/crystalBall-web/user/UserFlow'
        data = {
            "cycle_id": 202004,
            "line": 3,
            "region": 10,
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.post(url=self.config.get_value('host.conf', 'host', 'url') + url, data=data)
        execpet={'from': None, 'end': None, 'line': None, 'region': None, 'pageSize': None, 'pageIndex': None, 'startRow': None,
         'endRow': None, 'cycle_id': None, 'data_cycle': '1', 'own_corp_std_org_code': None,
         'std_prod_line_ver_code': None, 'ind_code': None, 'active_rate': 0.0, 'new_user_cnt': None,
         'loyal_user_cnt': None, 'active_user_cnt': None, 'low_active_user_cnt': None, 'no_active_user_cnt': None,
         'back_user_cnt': None, 'silent_user_cnt': None, 'sleep_user_cnt': None, 'lose_user_cnt': None,
         'source': '新增_202004', 'target': '忠诚_202005', 'value': 597}
        assert len(response.json()['data']) >= 1
        assert execpet ==response.json()["data"]['folders'][0]




if __name__ == '__main__':

    pytest.main(['test_userPath.py'])
