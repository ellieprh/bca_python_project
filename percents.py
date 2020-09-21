#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:57:37 2020

@author: elliebear
"""


decimals = [0.02, 0.3, 0.456]

# Convert to precentages
percents = []
for i in decimals:
    percents.append(i * 100)
print(percents)


# List Comprehension
percents = [i * 100 for i in decimals]

import numpy as np
np_decimals = np.array(decimals)
np_percents = np_decimals * 100
print(np_percents)

print(np_percents.mean())
print(np_percents.std())

