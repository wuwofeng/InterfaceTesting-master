#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

# 2. 参数传递
# (1) 传参参数为字典形式: 数据字典会在发送请求时会自动编码为表单形式
def transfer_dict_parameter():
    payload = {
        'key1': 'value1',
        'key2': 'value2'
    }

    transfer_dict_parameter_result = requests.post('https://httpbin.org/post', params=payload)
    print("transfer_dict_parameter_url: ", transfer_dict_parameter_result.url)
    print("transfer_dict_parameter_text: ", transfer_dict_parameter_result.text)


transfer_dict_parameter()


# (2) 传参参数为元组形式: 应用于在表单中多个元素使用同一 key 的时候
def transfer_tuple_parameter():
    payload = (
        ('key1', 'value1'),
        ('key1', 'value2')
    )

    transfer_tuple_parameter_result = requests.post('https://httpbin.org/post', params=payload)
    print('transfer_tuple_parameter_url: ', transfer_tuple_parameter_result.url)
    print('transfer_tuple_parameter_text: ', transfer_tuple_parameter_result.text)


transfer_tuple_parameter()


# (3) 传参参数形式是字符串形式
def transfer_string_parameter():
    payload = {
        'string1': 'value'
    }

    transfer_string_parameter_result = requests.post('https://httpbin.org/post', params=payload)
    print('transfer_string_parameter_url: ', transfer_string_parameter_result.url)
    print('transfer_string_parameter_text: ', transfer_string_parameter_result.text)


transfer_string_parameter()


# (4) 传参参数形式：一个多部分编码（Multipart-Encoded）的文件
def transfer_multipart_encoded_file():
    interface_url = 'https://httpbin.org/post'
    files = {
        # 显示设置文件名、文件类型和请求头
        'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})
    }

    transfer_multipart_encoded_file_result = requests.post(url=interface_url, files=files)
    print('transfer_multipart_encoded_file_result_url: ', transfer_multipart_encoded_file_result.url)
    print('transfer_multipart_encoded_file_result_url: ', transfer_multipart_encoded_file_result.text)


transfer_multipart_encoded_file()


