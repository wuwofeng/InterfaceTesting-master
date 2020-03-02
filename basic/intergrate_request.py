#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#集成多种请求方法

import requests
import json


class IntergrateRequest(object):
    # 请求 request方法
    def get_req(self, url, data=None, header=None):
        if header is not None:
            res = requests.get(url, data=json.loads(data), headers=header)
        else:
            res = requests.get(url, data=json.loads(data))
        return res.json()

    # post 请求方式
    def post_req(self, url, data=None, header=None):
        if header is not None:
            res = requests.post(url=url, data=json.loads(data), headers=header)
            #测试res的值
            # print(res)
            # print(res.json()['code'])
        else:
            res = requests.post(url=url, data=json.loads(data))
        try:
            return res.json()
        except json.JSONDecodeError as e:
            return None

    # delete 请求方式
    def delete_req(self, url, data=None, header=None):
        if header is not None:
            res = requests.delete(url, data=json.loads(data), headers=header)
        else:
            res = requests.delete(url, data=json.loads(data))
        return res.json()

    def main_req(self, method, url, data, header):
        if method == "get" or method == "GET":
            res = self.get_req(url, data, header)
        elif method == "post" or method == "POST":
            res = self.post_req(url, data, header)
        elif method == "delete" or method == "DELETE":
            res = self.delete_req(url, data, header)
        else:
            res = "你的请求方式暂未开放，请耐心等待"
        return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == "__main__":
    ir = IntergrateRequest()
    # get_method = 'get'
    # get_url = 'http://127.0.0.1:8000/query_article/'
    # get_data = None
    # get_header = None
    # print(ir.main_req(get_method, get_url, get_data, get_header))

    post_method = 'post'
    post_url = 'http://aomi-pay-manager-gateway-ingress.cf93fe1dde8584346a2d81575c79aff9e.cn-shenzhen.alicontainer.com/aomi-pay-manager/manager/merchantListAll'
    post_payload ={
        'bankMerchantId':'',
        'merchantName':'',
        'approvalStatus':'[]',
        'pageNo':'1',
        'merchantType':'',
        'timestamp':'1582855251411',
        }
    headers = {
        "Host": "aomi-pay-manager-gateway-ingress.cf93fe1dde8584346a2d81575c79aff9e.cn-shenzhen.alicontainer.com",
        "Content-Length": "99",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sessionId": "949918",
        "Origin": "http://test.manager.aomiapp.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "requestTime": "1582863782899",
        "channel": "99",
        "token": "120000008:1590639767283:21687a62bcc9e124ab8664f0c24d3468",
        "sign": "60d3e3e9661446e0eccfc251bb071c78",
        "Referer": "http://test.manager.aomiapp.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
    }
    ir.main_req(post_method, post_url, post_payload, headers)
 #   print(res.json())
    print(ir.main_req(post_method, post_url, post_payload, headers))
