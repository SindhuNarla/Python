# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:14:39 2019

@author: sindhunaidun
"""

import os

def add():
    '''this is the help of add'''
    print("this is add")
def copyfile(source, destination):
    
    '''this is the help of copyfile'''
    #print("this is openfile")
def readfile():
    print("this is readfile")
def delete(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("Successfully deleted")
    else:
        print("The file does not exist")
def listfiles(path):
    for r, d, f in os.walk(path):
        print("List of files are :\n")
        for filename in f:
            if os.path.isfile(filename):
                print(filename)
            
    