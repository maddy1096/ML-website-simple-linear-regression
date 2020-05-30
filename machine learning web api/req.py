# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:51:06 2020

@author: Mudhurika
"""

import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'year':5})

print(r.json())