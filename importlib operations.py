# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:22:38 2019

@author: sindhunaidun
"""

import os
import datetime
import calendar
''' list of all files and directories  '''
p = os.listdir("C:\\Users\\sindhunaidun\\Python examples")
#p = os.scandir("C:\\Users\\sindhunaidun\\Python examples")
#print(p)

''' to display files from the directory'''
for r, d, f in os.walk(r"C:\Users\sindhunaidun\Python examples"):
    for file in f:
        '''print(file)'''
        
''' display all files and size from current directory '''

for r, d, f in os.walk(r"C:\Users\sindhunaidun\Python examples"):
    for file in f:
        #print(file)
        if os.path.isfile(file):
            e = os.stat(file).st_size
            g = os.path.getsize(file)
            #print(file, g)
#d = os.stat(r"C:\Users\sindhunaidun\Python examples").st_size
#print(d)
w = os.getlogin()
print("Current user is : " ,w) 
d = os.getcwd()
print("Current working directory : ",d)
t = datetime.datetime.now()
print("Date time : ",t)
ti = t.time()
print("Timestamp : " ,ti)
#tm = input("which month calendar: " )
print("Calendar: ", calendar.month(2019, 10))

for r, d, f in os.walk(r"C:\Users\sindhunaidun\Python examples"): 
    print("No of files in the directory : ", len(f))



