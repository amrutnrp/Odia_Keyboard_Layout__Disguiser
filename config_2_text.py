# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:36:50 2021

@author: amrut
"""

from pyexcel_ods import get_data

right_side_margin = 9

sheet = get_data("backend_Config.ods")
file_csv = open ('map_config.csv','w')

# Cap_letters = sheet['map'][1][1:]
# small_letters = sheet['map'][2][1:]
num_and_symbols = sheet['map'][3][1:]
hex_codes = sheet['map'][4][1:]
num_and_symbols_preMap = sheet['map'][5][1:]
negative_symbol_map = sheet['map'][6][1:]


text_map = sheet['opcodes'][1:]
text_LUT = []
text_map2 = []

for Rows in text_map:
    if len(Rows) < right_side_margin:
        continue
    Rows2 = Rows [:right_side_margin]
    alpha = Rows2 [0][0]
    text_LUT.append(   ord (alpha) -97  )
    text_map2.append (Rows2 )

Odia_chr = ['']
Neg_chr = ['']
for hexnum in hex_codes:
    Odia_chr.append ( str(int (hexnum,16))  )
for hexnum in negative_symbol_map:
    Neg_chr.append ( str(int (hexnum,16)) )
    
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
                    string_sum=string_sum + '*'+Odia_chr [i]
                else:
                    string_sum=string_sum + '*' +Neg_chr [-i]
            string_sum = string_sum [1:]
        # print (string_sum)
        arr_out.append (string_sum)
    return arr_out
file_csv.write('#\n')

for index_i in range (26):
    item = text_map2 [ text_LUT .index (index_i) ]
    a= (item [1:])
    b= get_eq_char(a)
    append_str =  item[0] + ',' +','.join(b) + '\n'
    file_csv .write ( append_str )

file_csv.write('#Numbers Map\n')

other_map_list  = get_eq_char(num_and_symbols_preMap )
for i in range (len(num_and_symbols)):
    append_str =  str ( num_and_symbols [i] )  + ','+ other_map_list [i] + '\n'
    file_csv .write ( append_str )
    
















file_csv.close()