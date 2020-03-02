#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import requests

# 1.requests请求方式
# (1) GET请求方式
httpbin_get = requests.get('http://httpbin.org/get', data={'key': 'value'})
print('httpbin_get: ', httpbin_get.text)

# (2) POST请求方式
httpbin_post = requests.post('https://httpbin.org/post', data={'key': 'value'})
print('httpbin_post: ', httpbin_post.text)

# (3) PUT请求方式
httpbin_put = requests.put('https://httpbin.org/put', data={'key': 'value'})
print('httpbin_put: ', httpbin_put.text)

# (4) DELETE请求方式
httpbin_delete = requests.delete('https://httpbin.org/delete', data={'key': 'value'})
print('httpbin_delete', httpbin_delete)

# (5) PATCH亲求方式
httpbin_patch = requests.patch('https://httpbin.org/patch', data={'key': 'value'})
print('httpbin_patch', httpbin_patch)
