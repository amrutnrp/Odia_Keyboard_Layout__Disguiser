# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:16:26 2021

@author: amrut
"""
from Static_data import  *
# from config_2_text import i
file_csv = open ('map_config.csv','r')

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
        
        push_LUT (counter, 0, b[0])
        push_LUT (counter, 1, b[1])
        push_LUT (counter, 2, b[2])
        push_LUT (counter, 3, b[3])
        push_LUT (counter, 4, b[4])
        
        if b[6] == '':
            pass
        else:
            Dict_special_symbol_map [ control_inp_types[  ord (line[0]) -97] ] = b[6]
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