# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:55:32 2016

@author: xinruyue
"""
import jieba
from pypinyin import lazy_pinyin

#将汉字转化成拼音
with open('cap_pro.txt','r') as cp:
     with open('py_cap_pro.txt','w') as pcp:
             for each in cp:
                     ly_py = lazy_pinyin(each)
                     for each in ly_py:
                             pcp.write(each)
#拼音首字母大写
with open('pinyin.txt','r') as py:
     with open('cap_pinyin','w') as cpy:
             for each in py:
                     each = each.capitalize()
                     cpy.write(each)