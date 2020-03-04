import requests
import json
from hashlib import md5

from util.operate_json import OperateJson
class Login(object):
    def __init__(self):
        self.url = 'http://test.payapi.aomiapp.com/aomi-sc-uc/uc/login/ucLogin'
        # self.data = {
        #     'loginId': 'test',
        #     'password': 'E10ADC3949BA59ABBE56E057F20F883E',
        #     'systemId': '1',
        #     'sessionId': '688561',
        #     'timestamp': '1583117559708',
        # }
        self.data = OperateJson(r'C:\Users\FENG\Desktop\InterfaceTesting\data\LoginWord.json').get_json()
        self.header = OperateJson(r'C:\Users\FENG\Desktop\InterfaceTesting\data\LoginHeaders.json').get_json()
        # self.header = {
        #     "Accept": "application/json, text/plain, */*",
        #     "channel": "99",
        #     "Origin": "http://test.manager.aomiapp.com",
        #     "Referer": "http://test.manager.aomiapp.com/",
        #     "requestTime": "1583117559708",
        #     "sessionId": "undefined",
        #     "sign": "920f3326294cbaca00450fd710fb38c6",
        #     "token": "",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        # }
    def login(self):
        res =requests.post(url=self.url, data=self.data,headers=self.header)
        token = res.json()['result']['token']
        sessionId = self.data['sessionId']
        #sign的加密方法：md5(timestamp + 'sdf59s4d$JKf-/sdf23fwf')
        timestamp = self.data['timestamp']
        prMd5 = timestamp + 'sdf59s4d$JKf-/sdf23fwf'
        sign = md5(prMd5.encode(encoding='UTF-8')).hexdigest()
        return token,sessionId,sign

if __name__ == "__main__":
    token = Login().login()

