# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:05:29 2020

@author: vishal
"""


with open("file.txt") as f:
    with open("file1.txt", "w") as f1:
        for line in f:
            f1.write(line)
f=open("file.txt")
print("this content of old file")
print(f.read())   
print("this the content of copied file")
f1=open("file1.txt")
print(f1.read())         
            