# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:20:46 2021

@author: amrut
"""

control_inp_types = [
"'\\x01'",     #A
"'\\x02'",     #B 
"'\\x03'",     #C 
"'\\x04'",     #D 
"'\\x05'",     #E 
"'\\x06'",     #F 
"'\\x07'",     #G 
"'\\x08'",     #H
"'\\t'"  ,     #I
"'\\n'"  ,     #J  
"'\\x0b'",     #K  
"'\\x0c'",     #L  
"'\\r'" ,       #M
"'\\x0e'",     #N 
"'\\x0f'",     #O 
"'\\x10'",     #P 
"'\\x11'",     #Q 
"'\\x12'",     #R 
"'\\x13'",     #S  
"'\\x14'",     #T 
"'\\x15'",     #U
"'\\x16'",     #V 
"'\\x17'",     #W
"'\\x18'",     #X 
"'\\x19'",     #Y
"'\\x1a'"     #Z 
    ]


right_side_margin = 8
threshold_class0_end = 5
threshold_class1_end = 14
threshold_class2_end = 20
threshold_class3_end = 24

class0_Column_length = 3
class1_Column_length = 4
class2_Column_length = 6
class3_Column_length = 6

space_emphasis_map = {
    104:(0,'x'),
    97:(1,'a'),
    65:(2,'a'),
    101:(3, 'e'),
    117:(3,'u'),
    105:(3,'i'),
    111:(3,'o'),
    102:(1,'q')
    
    }
