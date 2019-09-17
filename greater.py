#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:26:13 2019

@author: susmit
"""

from string import ascii_lowercase as letters
from collections import Counter


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    if w == "".join(sorted(list(w),reverse=True)):
        return "no answer"

    a_to_d = {i:j for i,j in zip(letters,range(1,27))}
    #print(a_to_d)
    d_to_a = {j:i for i,j in a_to_d.items()}
    #print(d_to_a)
    s_num = int("".join([str(a_to_d[i]) for i in w]))
    print(s_num)
    last = int("".join(sorted(list(str(s_num)),reverse=True)))
    print(last)
    c = Counter(w)
    print(c)
    for num in range(s_num+1,last+1):
        if "0" not in str(num):
            if num == 48113:
                print("Error occurs here, you are splitting by each digit")
            c1 = Counter("".join([d_to_a.get(int(i)) for i in str(num)]))
            if not c - c1: 
                print(num)
                return "".join([d_to_a.get(int(i)) for i in str(num)])
            
biggerIsGreater("dhck")