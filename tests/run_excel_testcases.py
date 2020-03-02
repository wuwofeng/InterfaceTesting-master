#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import sys
import os
import json

curPath = os.path.abspath(os.path.dirname(__file__))
#print(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
#print('rootPath: ', rootPath)

from basic.get_excel_testcases import GetExcelTestcases
from basic.intergrate_request import IntergrateRequest
from util.email_config import EmailConfig
from util.operate_json import OperateJson
from util.compare_str import CompareStr
from util.update_json import  UpdateJson



class RunExcelTestcases(object):
    def __init__(self):
        #填写使用的xls文件路径，不填写默认使用TestcasesKeyword.xls
        self.gtc = GetExcelTestcases()
        self.ir = IntergrateRequest()
        self.ec = EmailConfig()
        #填写使用的json文件路径，不填写默认使用TestcaseHeaders2.json
        self.oj = OperateJson(r'C:\Users\FENG\Desktop\InterfaceTesting\data\TestcaseHeaders3.json')
        self.oj = OperateJson()
        self.cs = CompareStr()
        self.ud = UpdateJson()

    # 执行测试用例
    def run_testcases(self):
        #首先执行登录初始化操作
        self.ud.update_json()
        # 定义空列表，存放执行成功、失败和不执行的测试用例
        pass_lists = []
        fail_lists = []
        no_execute_lists = []
        # 获取总的用例条数
        cases_num = self.gtc.get_cases_num()
        # 遍历执行每一条测试用例
        for case in range(1, cases_num):
            # 用例是否执行
            is_run = self.gtc.get_is_run(case)
            # 接口的请求方式
            method = self.gtc.get_method(case)
            # 请求测试接口
            url = self.gtc.get_url(case)
            # 要请求的数据
            data = self.gtc.get_payload(case)
            # 取出 header--调用operate_json.py进行操作
            if case == 0:
                header = None
            else:
                # header = {
                #     "Host": "aomi-pay-manager-gateway-ingress.cf93fe1dde8584346a2d81575c79aff9e.cn-shenzhen.alicontainer.com",
                #     "Content-Length": "99",
                #     "Pragma": "no-cache",
                #     "Cache-Control": "no-cache",
                #     "sessionId": "949918",
                #     "Origin": "http://test.manager.aomiapp.com",
                #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                #     "Content-Type": "application/x-www-form-urlencoded",
                #     "Accept": "application/json",
                #     "requestTime": "1582863782899",
                #     "channel": "99",
                #     "token": "120000008:1590639767283:21687a62bcc9e124ab8664f0c24d3468",
                #     "sign": "60d3e3e9661446e0eccfc251bb071c78",
                #     "Referer": "http://test.manager.aomiapp.com/",
                #     "Accept-Encoding": "gzip, deflate",
                #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                #     "Connection": "keep-alive",
                # }
                header = self.oj.get_json()
            # 获取预期结果值 expected_result---这个实际测试中比较难处理，因为很多预期结果值都很难手写出来
            expected_result = self.gtc.get_expected_result(case)
            #IS_EXECUTE的值Yes开始执行
            if is_run is True:
                #调用intergrate_request.py进行request请求
                res = self.ir.main_req(method, url, data, header)
                #转换res的数据使得对比接口返回数据的时候能校验返回的其它内容
                res2 =json.loads(res)
                #调用compare_str.py进行预期结果和实际结果比较返回True或者False
                #if True写入pass到文档中
                if self.cs.is_contain(expected_result, res, res2):
                    self.gtc.write_actual_result(case, 'pass')
                    pass_lists.append(case)
                #if Flase写入返回的内容到文档中，case是行，res是返回结果
                else:
                    self.gtc.write_actual_result(case, res)
                    fail_lists.append(case)
            # IS_EXECUTE的值不为Yes
            else:
                no_execute_lists.append(case)
        print("没有执行的测试用例有, 按序号有：", no_execute_lists)
        #发送邮件
        self.ec.send_mail(pass_lists, fail_lists, no_execute_lists)
        print("....邮件已发送成功...")
        # print("---邮件尚未发送---")


if __name__ == "__main__":
    rts = RunExcelTestcases()
    rts.run_testcases()
    print("...程序已执行完毕,如果发送了文件请查阅文件内容...")
