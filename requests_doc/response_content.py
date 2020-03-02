#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests


# 1. 返回接口状态码：
# (1). 返回接口状态码：200
def response_200_code():
    interface_200_url = 'https://httpbin.org/status/200'
    response_get = requests.get(interface_200_url)
    response_get_code = response_get.status_code
    print('response_get_code: ', response_get_code)


response_200_code()


# (2).返回接口状态码：400
def response_400_code():
    interface_400_url = 'https://httpbin.org/status/400'
    response_get = requests.get(interface_400_url)
    response_get_code = response_get.status_code
    print('response_get_code: ', response_get_code)


response_400_code()


# (3) 重定向接口返回状态码：301
def response_301_code():
    interface_url = 'https://butian.360.cn'
    response_get = requests.get(interface_url)
    response_get_code = response_get.status_code
    print('response_get_code: ', response_get_code)


response_301_code()


# ------------------------------------------------------
# 2. 响应内容
def response_contents():
    url = 'https://httpbin.org/get'

    response_get = requests.get(url=url)

    # 响应头
    print('response_get_headers', response_get.headers)

    # 响应文本
    print('response_get_text: ', response_get.text)

    # 文本编码方式
    print('response_get_encoding: ', response_get.encoding)

    # 二进制响应内容
    print('response_get_content: ', response_get.content)

    # 原始响应内容
    origin_content = response_get.raw
    origin_content_read = origin_content.read(10)
    print('origin_content: ', origin_content)
    print('origin_content_read: ', origin_content_read)


response_contents()

