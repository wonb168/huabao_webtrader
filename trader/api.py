#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import requests

class TraderApi():
    """
    交易api类
    """
    URL_BASE = "https://m.touker.com/trading/"

    API_DICT = {
        "ENTRUST":"securitiesEntrust.json",
    }

    def __init__(self,cookies):
        """
        传入cookie
        cookie 字符串里面 _e_ 里面的"前面的反斜线需要保留,下面是正确示例
        '_e_': '"{\\\\"id\\\\":\\\\"8B6E72EB4E1FDDDD\\\\",\\\\"_e_\\\\":\\\\"653732DF6C3858D7ABF14C86E611846D\\\\",\\\\"_sign_\\\\":\\\\"27630C84\\\\"}"', 'ssid': '"5S3ASI2n5Hk="', '_s_': '"{\\\\"id\\\\":\\\\"8B6E72EB4E1FDDDD\\\\",\\\\"_e_\\\\":\\\\"653732DF6C3858D7ABF14C86E611846D\\\\",\\\\"_sign_\\\\":\\\\"14D8CA0A\\\\"}"',
        """
        self.cookies = cookies

    def entrust(self,stock_name,
                     stock_code,
                     exchange,
                     security_type,
                     price,
                     num,
                     entrust_type,
    ):
        """

        """
        return self.requests(
            'ENTRUST',
            {
                "stockName":stock_name,
                "stockCode":stock_code,
                "exchange":exchange,
                "securityType":security_type,
                "price":price,
                "num":num,
                "entrustType":entrust_type,
                "channel":"",
                "deviceInfo":'',
            }
        )

    def requests(self,api,json):
        print(self.URL_BASE + self.API_DICT[api])
        cookies = {}
        for item in self.cookies.split('; '):
            k,v = item.split('=',1)
            cookies[k] = v
        print(cookies)
        return requests.post(self.URL_BASE + self.API_DICT[api], data=json, cookies=cookies)




