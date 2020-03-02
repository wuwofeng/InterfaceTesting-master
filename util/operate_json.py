#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
import os
#当前路径
curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
#根路径
rootPath = os.path.abspath(os.path.dirname(curPath))
print(rootPath)

#操作的json文件的路径
class OperateJson(object):
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            #配置使用的json文件名称和路径
            self.file_name = r"data/TestcaseHeaders2.json"
            self.file_name = os.path.join(rootPath, self.file_name)
            print("self.file_name: ", self.file_name)

        self.data = self.get_json()

    # 读取 json 文件
    def get_json(self):
        with open(self.file_name, encoding='utf-8') as fp:
            data = json.load(fp)
        return data
    # 根据关键词读取数据
    def get_key_data(self, key):
        return self.data[key]


if __name__ == '__main__':
    oj = OperateJson("../data/TestcaseHeaders2.json")
    print(oj.get_json())
    print(type(oj))
    print(oj.data)
