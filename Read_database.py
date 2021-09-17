# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 01:57:11 2021

@author: amrutnp
"""

Odia_data2 = []

# open file and read the content in a list
with open('Odia_data.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        Odia_data2.append(currentPlace)