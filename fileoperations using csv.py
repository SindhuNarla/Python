# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:10:59 2019

@author: sindhunaidun
"""

import csv

fobj = open(r"C:\Users\sindhunaidun\Python examples\samplecsvtransactions12.csv", "r")
reader = csv.reader(fobj)

for line in reader:
    print(line)
fobj = open(r"C:\Users\sindhunaidun\Python examples\samplecsvtransactions12.csv", "r")
print(fobj.readlines())
fobj.close()