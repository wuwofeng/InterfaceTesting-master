#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class CompareStr(object):
    #str1是预期结果，str2是request返回内容
    def is_contain(self, str1, str2, str3):
        """
        判断预期结果是否和实际结果相同
        :param str1: 预期结果值
        :param str2: 实际结果值
        :param str3: 返回码的code，根据实际需要填写
        :return: flag
        """
        if str1 in str2 and str3['code'] == '200':
            flag = True
        else:
            flag = False
        return flag


if __name__ == "__main__":
    cs = CompareStr()
    str = {"code": '200'}
    print(cs.is_contain("abc", "abcedf", str))
