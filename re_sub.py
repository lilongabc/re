#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/4/1

#替换匹配内容
import re

pattern = re.compile(r"(\w+) (\w+)")
str = "hello 123,hello 999"
result = pattern.sub("hello world",str)

print result
# pirnt result : hello world,hello world

