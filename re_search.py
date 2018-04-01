#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/4/1

import re
#匹配至少一个或者无限多个数字
pattern = re.compile(r"\d+")
result = pattern.search(r"aaa123bbb456")
print result.group()