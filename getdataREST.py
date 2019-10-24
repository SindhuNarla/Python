# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:21:29 2019

@author: sindhunaidun
"""

import requests
response = requests.get('https://www.google.com')
print(response)
print(response.status_code)
#print(response.text)
