#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/4/1

import re
pattern = re.compile("[\s\d\\\:]+")
result = pattern.split(r"a bb\aa:mm;  a")
print result