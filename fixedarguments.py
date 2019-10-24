# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:49:39 2019

@author: sindhunaidun
"""

#fixed arguements
def display(first, second):
    print(first, second)


#display("sindhu", "narla")

#default arguments
def defaultdisplay(first = "hi", second = "hello"):
    print(first, second)
    return "success"

#defaultdisplay(1)

#keyword arg
def keydisplay(first, second):
    print(second, first)
    
#keydisplay(second = "narla", first= "sindhu")

#variable arg
def vardisplay1(**x):
    print(x)
    '''for i in info:
        print(i)'''

#vardisplay1(chap1=1, chap2=2)