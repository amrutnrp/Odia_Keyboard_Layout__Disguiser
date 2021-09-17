# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 01:57:37 2021

@author: amrutnp
"""


Odia_data= Odia_data_3
with open('Odia_data.txt', 'w') as filehandle:
    for listitem in Odia_data:
        if isinstance(listitem, str):
            filehandle.write(repr(listitem))
            print (repr(listitem))
        else:
            filehandle.write('%s\n' % listitem)
        
        
        