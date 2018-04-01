#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Li Long
# Date: 2018/4/1

'''
re NOTE
Python 里面re 模块有两种方式：
#将正则表达式编译成一个Pattern 规则对象（）里面是规则。
pattern = re.compile("\d")
然后通过下面方法进行相应的匹配。
pattern.match()   从起始位置往后查找，返回第一个符合规则的，只匹配一次。
math(str,begin,end) match里面的参数。
pattern.search()  从任何位置开始往后查找，返回第一个符合规则的，只匹配一次。
pattern.findall() 所有的全部匹配，返回一个列表。
pattern.finditer() 所有的全部匹配，返回一个迭代器，很少用到
pattern.split()   分割字符串，返回列表。
pattern.sub()     替换用

@@@正则表达式中，group（）用来提出分组截获的字符串，（）用来分组
1. 正则表达式中的三组括号把匹配结果分成三组
 group() 同group（0）就是匹配正则表达式整体结果
 group(1) 列出第一个括号匹配部分，
 group(2) 列出第二个括号匹配部分，
 group(3) 列出第三个括号匹配部分。
2. 没有匹配成功的，re.search（）返回None
3. 当然郑则表达式中没有括号，group(1)肯定不对了。

参数
re.I表示忽略大小写
re.S表示全文匹配
'''
import re
#匹配一个或者多个a-z a-z，两组单词，并且re.I参数是不区分大小写
#第一个字串Hello是group（1），第二个world是group(2)
pattern = re.compile(r"([a-z]+) ([a-z]+)",re.I)
result = pattern.match("Hello world hello Python")
print result.group(2)
#匹配内容的所以下标，输出为(0, 11)，也就是0位到10位
print result.span()
