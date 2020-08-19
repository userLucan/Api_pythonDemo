#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-07 14:09
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
        print('====执行完毕====')

    def test_ProductOrder(self):
        """校验订购信息"""
        url = '/crystalBall-web/user/ProductOrder'
        data = {
            "from": "202002",
            "end": "202008",
            "line": "3",
            "region": "10",
            "ind_code": "all",
            "pageIndex": "1",
            "pageSize": "20",
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.post(url=self.config.get_value('host.conf', 'host', 'url') + url, data=data)
        execpect = {'from': None, 'end': None, 'line': None, 'region': None, 'pageSize': None, 'pageIndex': None,
                    'startRow': None, 'endRow': None, 'cycle_id': '202003', 'own_corp_std_org_code': None,
                    'std_prod_line_ver_code': None, 'month_itv_type': None, 'vocation': None, 'ind_code': None,
                    'prod_id': None, 'prod_name': None, 'event_code': None, 'event_name': None,
                    'demand_type_code': None, 'demand_type_name': None, 'prod_user_cnt': 10408, 'hb_prod_user_cnt': 0.0,
                    'new_prod_user_cnt': 1878, 'new_prod_user_rate': 0.1781, 'hb_new_prod_user_rate': 0.0,
                    'vod_payuser_cnt': 16168, 'hb_vod_payuser_cnt': 0.0, 'prod_cnt': 20773, 'hb_prod_cnt': 0.0,
                    'vod_pay_cnt': 169166, 'hb_vod_pay_cnt': 0.0, 'pay_rate': 0.1591, 'hb_pay_rate': 0.0,
                    'prod_td_cnt': None, 'hb_prod_td_cnt': 0.0, 'vip_change_rate': 0.0, 'hb_vip_change_rate': 0.0,
                    'change_rate': 0.0, 'prod_line_user_cnt': None, 'hb_prod_line_user_cnt': 0.0,
                    'prod_online_user_cnt': None, 'hb_prod_online_user_cnt': 0.0, 'prod_activ_user_cnt': None,
                    'hb_prod_activ_user_cnt': 0.0, 'prod_inactiv_user_cnt': None, 'hb_prod_inactiv_user_cnt': 0.0,
                    'vod_cnt': None, 'hb_vod_cnt': 0.0, 'vod_user_cnt': 167045, 'hb_vod_user_cnt': 0.0,
                    'vod_per_cnt': 0.0, 'vod_per_duration': 0.0, 'vod_cycle_type': None,
                    'vod_first_demand_user_cnt': None}
        assert response.json()['data']['folders'][0] == execpect

    def test_ProductOrder02(self):
        """校验数据列表"""
        url = '/crystalBall-web/user/ProductOrder'
        data = {
            "from": "202004",
            "end": "202004",
            "line": "3",
            "region": "10",
            "ind_code": "all",
            "pageIndex": "1",
            "pageSize": "20",
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        execpect = {'from': None, 'end': None, 'line': None, 'region': None, 'pageSize': None, 'pageIndex': None,
                    'startRow': None, 'endRow': None, 'cycle_id': '202004', 'own_corp_std_org_code': None,
                    'std_prod_line_ver_code': None, 'month_itv_type': None, 'vocation': None, 'ind_code': None,
                    'prod_id': None, 'prod_name': None, 'event_code': None, 'event_name': None,
                    'demand_type_code': None, 'demand_type_name': None, 'prod_user_cnt': 9147,
                    'hb_prod_user_cnt': -0.1212, 'new_prod_user_cnt': 1554, 'new_prod_user_rate': 0.2597,
                    'hb_new_prod_user_rate': 0.4582, 'vod_payuser_cnt': 9505, 'hb_vod_payuser_cnt': -0.4121,
                    'prod_cnt': 18579, 'hb_prod_cnt': -0.1056, 'vod_pay_cnt': 119199, 'hb_vod_pay_cnt': -0.2954,
                    'pay_rate': 0.122, 'hb_pay_rate': -0.2332, 'prod_td_cnt': None, 'hb_prod_td_cnt': 0.0,
                    'vip_change_rate': 0.0, 'hb_vip_change_rate': 0.0, 'change_rate': 0.0, 'prod_line_user_cnt': None,
                    'hb_prod_line_user_cnt': 0.0, 'prod_online_user_cnt': None, 'hb_prod_online_user_cnt': 0.0,
                    'prod_activ_user_cnt': None, 'hb_prod_activ_user_cnt': 0.0, 'prod_inactiv_user_cnt': None,
                    'hb_prod_inactiv_user_cnt': 0.0, 'vod_cnt': None, 'hb_vod_cnt': 0.0, 'vod_user_cnt': 152860,
                    'hb_vod_user_cnt': -0.0849, 'vod_per_cnt': 0.0, 'vod_per_duration': 0.0, 'vod_cycle_type': None,
                    'vod_first_demand_user_cnt': None}
        assert response.json()['data']['folders'][0] == execpect

    def test_OrderLeaderboard(self):
        """校验产品订购量排行(202007)"""
        url = '/crystalBall-web/user/OrderLeaderboard'
        data = {
            "line": "3",
            "region": "10",
            "cycle_id": "202007",
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        execpect = {'from': None, 'end': None, 'line': None, 'region': None, 'pageSize': None, 'pageIndex': None,
                    'startRow': None, 'endRow': None, 'cycle_id': '202007', 'own_corp_std_org_code': None,
                    'std_prod_line_ver_code': None, 'month_itv_type': None, 'vocation': None, 'ind_code': None,
                    'prod_id': '10000008180', 'prod_name': '华数会员50元/月', 'event_code': None, 'event_name': None,
                    'demand_type_code': None, 'demand_type_name': None, 'prod_user_cnt': 4424,
                    'hb_prod_user_cnt': 0.0848, 'new_prod_user_cnt': None, 'new_prod_user_rate': 0.0,
                    'hb_new_prod_user_rate': 0.0, 'vod_payuser_cnt': None, 'hb_vod_payuser_cnt': 0.0, 'prod_cnt': 4557,
                    'hb_prod_cnt': 0.0868, 'vod_pay_cnt': None, 'hb_vod_pay_cnt': 0.0, 'pay_rate': 0.0,
                    'hb_pay_rate': 0.0, 'prod_td_cnt': 1244, 'hb_prod_td_cnt': 0.2089, 'vip_change_rate': 0.4222,
                    'hb_vip_change_rate': -0.0612, 'change_rate': 0.0, 'prod_line_user_cnt': 585,
                    'hb_prod_line_user_cnt': 0.1101, 'prod_online_user_cnt': 3842, 'hb_prod_online_user_cnt': 0.0807,
                    'prod_activ_user_cnt': 0, 'hb_prod_activ_user_cnt': 0.0, 'prod_inactiv_user_cnt': 585,
                    'hb_prod_inactiv_user_cnt': 0.1101, 'vod_cnt': None, 'hb_vod_cnt': 0.0, 'vod_user_cnt': None,
                    'hb_vod_user_cnt': 0.0, 'vod_per_cnt': 0.0, 'vod_per_duration': 0.0, 'vod_cycle_type': None,
                    'vod_first_demand_user_cnt': None}
        assert response.json()['data']['folders'][0] == execpect

    def test_Prodline(self):
        """校验产品名称"""
        url = '/crystalBall-web/user/Prodline?'
        data = {
            "line": "3",
            "region": "10",
            "cycle_id": "202007",
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert '全能享看45元/月' in response.json()[0]['prod_name']

    def test_ProductOrder03(self):
        """校验数据列表"""
        url = '/crystalBall-web/user/ProductOrder?'
        data = {
            "from": "202002",
            "end": "202008",
            "line": "3",
            "region": "10",
            "ind_code": "prod",
            # "prod_name":"",
            # "prod_id":"",
            "pageIndex": "1",
            "pageSize": "20",
            "_": "1596781427169",
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        execpet = {'from': None, 'end': None, 'line': None, 'region': None, 'pageSize': None, 'pageIndex': None,
                   'startRow': None, 'endRow': None, 'cycle_id': '202003', 'own_corp_std_org_code': None,
                   'std_prod_line_ver_code': None, 'month_itv_type': None, 'vocation': None, 'ind_code': None,
                   'prod_id': '10000008180', 'prod_name': '华数会员50元/月', 'event_code': None, 'event_name': None,
                   'demand_type_code': None, 'demand_type_name': None, 'prod_user_cnt': 5181, 'hb_prod_user_cnt': 0.0,
                   'new_prod_user_cnt': None, 'new_prod_user_rate': 0.0, 'hb_new_prod_user_rate': 0.0,
                   'vod_payuser_cnt': None, 'hb_vod_payuser_cnt': 0.0, 'prod_cnt': 5286, 'hb_prod_cnt': 0.0,
                   'vod_pay_cnt': None, 'hb_vod_pay_cnt': 0.0, 'pay_rate': 0.0, 'hb_pay_rate': 0.0, 'prod_td_cnt': 6899,
                   'hb_prod_td_cnt': 0.0, 'vip_change_rate': 0.4713, 'hb_vip_change_rate': 0.0, 'change_rate': 0.0,
                   'prod_line_user_cnt': 580, 'hb_prod_line_user_cnt': 0.0, 'prod_online_user_cnt': 4607,
                   'hb_prod_online_user_cnt': 0.0, 'prod_activ_user_cnt': 0, 'hb_prod_activ_user_cnt': 0.0,
                   'prod_inactiv_user_cnt': 580, 'hb_prod_inactiv_user_cnt': 0.0, 'vod_cnt': None, 'hb_vod_cnt': 0.0,
                   'vod_user_cnt': None, 'hb_vod_user_cnt': 0.0, 'vod_per_cnt': 0.0, 'vod_per_duration': 0.0,
                   'vod_cycle_type': None, 'vod_first_demand_user_cnt': None}
        assert execpet == response.json()['data']['folders'][0]

    def test_ProductOrderProdVod(self):
        """校验下游行为播变化(全能享看45元/月)"""
        url = '/crystalBall-web/user/ProductOrderProdVod'
        data = {
            "line": "3",
            "region": "10",
            "cycle_id": "202004",
            "prod_id": "10000006360",
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert len(response.json()['data']['folders'][0])>=1

    def test_ProductOrderProdVodDemand01(self):
        """校验下游行为播变化(全能享看45元/月)"""
        url = '/crystalBall-web/user/ProductOrderProdVodDemand'
        data = {
            "line": "3",
            "region": "10",
            "cycle_id": "202004",
            "prod_id": "10000006360",
            'vod_cycle_type': '本月',
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        execpect = {'from': None, 'end': None, 'line': None, 'region': None, 'pageSize': None, 'pageIndex': None, 'startRow': None, 'endRow': None, 'cycle_id': '202004', 'own_corp_std_org_code': None, 'std_prod_line_ver_code': None, 'month_itv_type': None, 'vocation': None, 'ind_code': None, 'prod_id': '10000006360', 'prod_name': '全能享看45元/月', 'event_code': None, 'event_name': None, 'demand_type_code': '12', 'demand_type_name': '娱乐', 'prod_user_cnt': None, 'hb_prod_user_cnt': 0.0, 'new_prod_user_cnt': None, 'new_prod_user_rate': 0.0, 'hb_new_prod_user_rate': 0.0, 'vod_payuser_cnt': None, 'hb_vod_payuser_cnt': 0.0, 'prod_cnt': None, 'hb_prod_cnt': 0.0, 'vod_pay_cnt': None, 'hb_vod_pay_cnt': 0.0, 'pay_rate': 0.0, 'hb_pay_rate': 0.0, 'prod_td_cnt': None, 'hb_prod_td_cnt': 0.0, 'vip_change_rate': 0.0, 'hb_vip_change_rate': 0.0, 'change_rate': 0.0, 'prod_line_user_cnt': None, 'hb_prod_line_user_cnt': 0.0, 'prod_online_user_cnt': None, 'hb_prod_online_user_cnt': 0.0, 'prod_activ_user_cnt': None, 'hb_prod_activ_user_cnt': 0.0, 'prod_inactiv_user_cnt': None, 'hb_prod_inactiv_user_cnt': 0.0, 'vod_cnt': 42, 'hb_vod_cnt': 0.0, 'vod_user_cnt': 1, 'hb_vod_user_cnt': 0.0, 'vod_per_cnt': 42.0, 'vod_per_duration': 1121.6667, 'vod_cycle_type': '本月', 'vod_first_demand_user_cnt': None}
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        assert response.json()['data']['folders'][0]==execpect

    def test_ProductOrderProdVodDemand02(self):
        """校验下游行为播变化(全能享看45元/月)"""
        url = '/crystalBall-web/user/ProductOrderProdVodDemand'
        data = {
            "line": "3",
            "region": "10",
            "cycle_id": "202004",
            "prod_id": "10000006360",
            'vod_cycle_type': '上月',
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        expect = {'from': None, 'end': None, 'line': None, 'region': None, 'pageSize': None, 'pageIndex': None, 'startRow': None, 'endRow': None, 'cycle_id': '202004', 'own_corp_std_org_code': None, 'std_prod_line_ver_code': None, 'month_itv_type': None, 'vocation': None, 'ind_code': None, 'prod_id': '10000006360', 'prod_name': '全能享看45元/月', 'event_code': None, 'event_name': None, 'demand_type_code': '12', 'demand_type_name': '娱乐', 'prod_user_cnt': None, 'hb_prod_user_cnt': 0.0, 'new_prod_user_cnt': None, 'new_prod_user_rate': 0.0, 'hb_new_prod_user_rate': 0.0, 'vod_payuser_cnt': None, 'hb_vod_payuser_cnt': 0.0, 'prod_cnt': None, 'hb_prod_cnt': 0.0, 'vod_pay_cnt': None, 'hb_vod_pay_cnt': 0.0, 'pay_rate': 0.0, 'hb_pay_rate': 0.0, 'prod_td_cnt': None, 'hb_prod_td_cnt': 0.0, 'vip_change_rate': 0.0, 'hb_vip_change_rate': 0.0, 'change_rate': 0.0, 'prod_line_user_cnt': None, 'hb_prod_line_user_cnt': 0.0, 'prod_online_user_cnt': None, 'hb_prod_online_user_cnt': 0.0, 'prod_activ_user_cnt': None, 'hb_prod_activ_user_cnt': 0.0, 'prod_inactiv_user_cnt': None, 'hb_prod_inactiv_user_cnt': 0.0, 'vod_cnt': 27, 'hb_vod_cnt': 0.0, 'vod_user_cnt': 1, 'hb_vod_user_cnt': 0.0, 'vod_per_cnt': 27.0, 'vod_per_duration': 943.8333, 'vod_cycle_type': '上月', 'vod_first_demand_user_cnt': None}
        assert response.json()['data']['folders'][0]==expect

    def test_ProductOrderProdVodDemand03(self):
        """校验下游行为播变化(全能享看45元/月)"""
        url = '/crystalBall-web/user/ProductOrderProdVodDemand'
        data = {
            "line": "3",
            "region": "10",
            "cycle_id": "202004",
            "prod_id": "10000006360",
            'vod_cycle_type': '后一个月',
            "token": self.config.get_value('cookie.conf', 'token', 'token')
        }
        response = requests.get(url=self.config.get_value('host.conf', 'host', 'url') + url, params=data)
        expect = {'from': None, 'end': None, 'line': None, 'region': None, 'pageSize': None, 'pageIndex': None, 'startRow': None, 'endRow': None, 'cycle_id': '202004', 'own_corp_std_org_code': None, 'std_prod_line_ver_code': None, 'month_itv_type': None, 'vocation': None, 'ind_code': None, 'prod_id': '10000006360', 'prod_name': '全能享看45元/月', 'event_code': None, 'event_name': None, 'demand_type_code': '17', 'demand_type_name': '电视剧', 'prod_user_cnt': None, 'hb_prod_user_cnt': 0.0, 'new_prod_user_cnt': None, 'new_prod_user_rate': 0.0, 'hb_new_prod_user_rate': 0.0, 'vod_payuser_cnt': None, 'hb_vod_payuser_cnt': 0.0, 'prod_cnt': None, 'hb_prod_cnt': 0.0, 'vod_pay_cnt': None, 'hb_vod_pay_cnt': 0.0, 'pay_rate': 0.0, 'hb_pay_rate': 0.0, 'prod_td_cnt': None, 'hb_prod_td_cnt': 0.0, 'vip_change_rate': 0.0, 'hb_vip_change_rate': 0.0, 'change_rate': 0.0, 'prod_line_user_cnt': None, 'hb_prod_line_user_cnt': 0.0, 'prod_online_user_cnt': None, 'hb_prod_online_user_cnt': 0.0, 'prod_activ_user_cnt': None, 'hb_prod_activ_user_cnt': 0.0, 'prod_inactiv_user_cnt': None, 'hb_prod_inactiv_user_cnt': 0.0, 'vod_cnt': 260, 'hb_vod_cnt': 0.0, 'vod_user_cnt': 1, 'hb_vod_user_cnt': 0.0, 'vod_per_cnt': 260.0, 'vod_per_duration': 6073.0667, 'vod_cycle_type': '后一个月', 'vod_first_demand_user_cnt': None}
        assert response.json()['data']['folders'][0] == expect


if __name__ == '__main__':
    pytest.main()
