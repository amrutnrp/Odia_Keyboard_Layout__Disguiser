# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:16:26 2021

@author: amrut
"""

# from config_2_text import i
file_csv = open ('map_config.csv','r')


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


result_LUT = ['']*(26*8+2)
def get_exact_char (arr_in):
    arr_out =[]
    for pointer in arr_in:
        string_sum = ''
        if pointer == '':
            arr_out.append ('')
            continue
        list_all_pointers = pointer.split('*')
        for item in list_all_pointers:
            i = int (item)
            string_sum=string_sum + chr (i) 
        # print (string_sum)
        arr_out.append (string_sum)
    return arr_out
def push_LUT(row_mode, col, dataIN):
    global result_LUT
    result_LUT [row_mode*26+col]= dataIN

space_emphasis_map= {}
Dict_special_symbol_map= {}
Number_map = {}
number_result_ord = []
special_symbols = []
For_control = [''] * 26
mode = -1
counter = 0

for line in file_csv:
    a= line [:-1].split(',')
    
    if line [0] == '#':
        mode = mode +1
        continue
    elif mode ==0 :
        
        b=  get_exact_char (a [1:])
        
        push_LUT (0 ,counter, b[0])
        push_LUT (1 ,counter, b[1])
        push_LUT (2 ,counter, b[2])
        push_LUT (3 ,counter, b[3])
        push_LUT (4 ,counter, b[4])
        push_LUT (5 ,counter, b[5])
        push_LUT (6 ,counter, b[6])
        push_LUT (7 ,counter, b[7])
        counter = counter +1
        
        if b[6] == '':
            pass
        else:
            Dict_special_symbol_map [ control_inp_types[  ord (line[0]) -97] ] = b[6]
            special_symbols.append ( control_inp_types[  ord (line[0]) -97] )
        if b [7] == "":
            pass
        else:
            space_emphasis_map [ ord (line[0]) ] = b[7]
            
    elif mode ==1:  #numbers
        b=  get_exact_char ( [ a [1] ])
        Number_map [ a[0]] = b[0]
        number_result_ord.append ( ord (a[0]) )
        
space_emphasis_list = list(space_emphasis_map.keys())            
file_csv.close()
