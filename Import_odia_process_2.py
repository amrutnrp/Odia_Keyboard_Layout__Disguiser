# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:16:26 2021

@author: amrut
"""
from Static_data import  *
from pyexcel_ods import get_data

sheet = get_data("backend_Config.ods")

# Cap_letters = sheet['map'][1][1:]
# small_letters = sheet['map'][2][1:]
num_and_symbols = sheet['map'][3][1:]
hex_codes = sheet['map'][4][1:]
num_and_symbols_preMap = sheet['map'][5][1:]
negative_symbol_map = sheet['map'][6][1:]


text_map = sheet['opcodes'][1:]
text_LUT = [None]*26

for Rows in text_map:
    if len(Rows) < 8:
        continue
    alpha = Rows [0]
    LUTindex = Rows [right_side_margin]
    text_LUT [ord (alpha[0]) - 97 ]  = int (LUTindex)

Odia_chr = ['']
Neg_chr = ['']
for hexnum in hex_codes:
    Odia_chr.append ( chr(int (hexnum,16))  )
for hexnum in negative_symbol_map:
    Neg_chr.append ( chr(int (hexnum,16)) )
    
def get_eq_char (arr_in):
    arr_out =[]
    for pointer in arr_in:
        string_sum = ''
        if  isinstance (pointer, int) :
           
            if pointer> 0:
                string_sum =  Odia_chr [pointer]
            else:
                string_sum =  Neg_chr [-pointer]
        else:
            if pointer == '':
                arr_out.append ('')
                continue
            list_all_pointers = pointer.split('*')
            for item in list_all_pointers:
                i = int (item)
                if i> 0:
                    string_sum=string_sum + Odia_chr [i]
                else:
                    string_sum=string_sum + Neg_chr [-i]
        # print (string_sum)
        arr_out.append (string_sum)
    return arr_out

transpose_LUT = []
for item in text_map[2:]:
    if len (item) < 5:
        continue
    a= (item [1:right_side_margin])
    b= get_eq_char(a)
    transpose_LUT .append (b)

result_LUT = ['']*(30*8+2)
def push_LUT(row_mode, col, dataIN):
    global result_LUT
    result_LUT [row_mode*30+col]= dataIN
def get_LUT (row_mode, col):
    if 0 < col <= threshold_class0_end and row_mode < class0_Column_length :
        pass
    elif threshold_class0_end < col <= threshold_class1_end and row_mode < class1_Column_length :
        pass
    elif  threshold_class1_end < col <= threshold_class2_end and row_mode < class2_Column_length:   
        pass 
    elif threshold_class2_end < col <= threshold_class3_end and row_mode < class3_Column_length:
        pass
    else:
        print ('Invalid character call')
        raise KeyboardInterrupt 
        
    return result_LUT [row_mode*30+col]

temp_control_op = []

for i in range(len(transpose_LUT)):
    temp_control_op.append( transpose_LUT [i][right_side_margin -2])  #carrying it to shirt for 'control'
    for j in range(len(transpose_LUT[i])):
        # print (transpose_LUT[i][j])
        push_LUT(j,i,transpose_LUT[i][j])
        
result_LUT = [''] + result_LUT        
# adding a index to avoid -1 calc everytime

Dict_special_symbol_map = {}
for i in range(len(temp_control_op )):
    if not temp_control_op [i] == '':
        Dict_special_symbol_map [str ( control_inp_types [i] )] = temp_control_op [i] 

special_symbols = list(Dict_special_symbol_map.keys())  # ouan and iyan for control keys

Number_map = {}
temp_control_op = get_eq_char( num_and_symbols_preMap )
for i in range (len(num_and_symbols)):
    Number_map[str ( num_and_symbols [i] ) ] = temp_control_op [i]
        
