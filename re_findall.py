#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/4/1
#find all 是匹配所有内容，并发回成列表,因为是全部输出为列表，AttributeError: 'list' object has no attribute 'group'，所以没有group（）方法。
import re
#一个或者多个数字
pattern = re.compile(r"\d+")
result = pattern.findall("hello 123456 789")
print result
#结果['123456', '789']

#一个数字，匹配所有1个数字。会分别打印出列表，不符合的返回空列表
pattern1 = re.compile(r"\d?")
result1 = pattern1.findall("hello 123456 789")
print result1
#结果['', '', '', '', '', '', '1', '2', '3', '4', '5', '6', '', '7', '8', '9', '']

