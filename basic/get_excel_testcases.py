#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from util.operate_excel import OperateExcel
from basic import testcases_keyword


class GetExcelTestcases(object):
    def __init__(self):
        #调用operate_excel.py
        self.oe = OperateExcel()

    # 获取测试用例条数，也就是 Excel 中的行数
    def get_cases_num(self):
        return self.oe.get_sheet_nrows()

    # 判断是否携带 headers---直接调用operate_json来获取统一的token
    def is_header(self, row):
        col = int(testcases_keyword.get_header())
        header = self.oe.get_sheet_cell(row, col)
        if header is not None:
            return header
        else:
            print("你的 header 呢？")
            return None

    # 判断该条用例是否执行
    def get_is_run(self, row):
        col = int(testcases_keyword.get_is_execute())
        is_run = self.oe.get_sheet_cell(row, col)
        if is_run == '':
            flag = False
        else:
            flag = True
        return flag

    # 获取不同接口的请求方式
    def get_method(self, row):
        col = int(testcases_keyword.get_method())
        method = self.oe.get_sheet_cell(row, col)
        return method

    # 获取要测试的接口链接
    def get_url(self, row):
        col = int(testcases_keyword.get_interface_url())
        url = self.oe.get_sheet_cell(row, col)
        return url

    # 获取接口参数
    def get_payload(self, row):
        col = int(testcases_keyword.get_payload())
        payload = self.oe.get_sheet_cell(row, col)
        if payload is None:
            print(payload)
            return None
        return payload

    # 获取预期结果
    def get_expected_result(self, row):
        col = int(testcases_keyword.get_expected_result())
        expected_result = self.oe.get_sheet_cell(row, col)
        if expected_result is None:
            return None
        return expected_result

    # 写入实际结果
    def write_actual_result(self, row, value):
        col = int(testcases_keyword.get_actual_result())
        self.oe.write_to_excel(row, col, value)


if __name__ == "__main__":
    gety = GetExcelTestcases()
    # print(gety.get_cases_num())
    # print(gety.is_header(2))
    #print(gety.get_is_run(4))


