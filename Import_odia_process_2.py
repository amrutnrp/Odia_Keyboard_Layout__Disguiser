# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:16:26 2021

@author: amrut
"""
from Static_data import  *
from pyexcel_ods import get_data

sheet = get_data("backend_Config.ods")

Cap_letters = sheet['map'][1][1:]
small_letters = sheet['map'][2][1:]
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
Neg_chr = []
for hexnum in hex_codes:
    Odia_chr.append ( chr(int (hexnum,16))  )
for hexnum in negative_symbol_map:
    Neg_chr.append ( chr(int (hexnum,16)) )
    
def get_eq_char (arr_in):
    arr_out =[]
    for pointer in arr_in:
        string_sum = ''
        if  isinstance (pointer, int) :
            string_sum =  Odia_chr [pointer]
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
                    string_sum=string_sum + Neg_chr [i]
        arr_out.append (string_sum)
    return arr_out

transpose_LUT = []
for item in text_map[3:]:
    if len (item) < 5:
        continue
    a= (item [1:right_side_margin])
    b= get_eq_char(a)
    transpose_LUT .append (b)

result_LUT = ['']*(25*8+1)
def push_LUT(row_mode, col, dataIN):
    global result_LUT
    result_LUT [row_mode*25+col]= dataIN
def get_LUT (row_mode, col):
    return result_LUT [row_mode*25+col]


for i in range(len(transpose_LUT)):
    for j in range(len(transpose_LUT[i])):
        push_LUT(j,i,transpose_LUT[i][j])
        
        
        
        
        

''' 
# DEFINE DICTIONARIES
Odia_data_3= []
for item in Odia_data2:
    Odia_data_3.append(item.split(','))

Interpreted_LUT= []

master_Odia_LUT = ['']*len(Odia_data_3 [3])
master_gen_LUT = ['']*len(Odia_data_3 [9])
for j,i in enumerate (Odia_data_3 [3]):
    master_Odia_LUT [j] = chr(int (i,16))

for j,i in enumerate (Odia_data_3 [9]):
    if 'x' in i:
        master_gen_LUT [j] = chr(int (i,16))
    else:
        master_gen_LUT [j] = i
        
for i in [4,5,6,7,8, 11,12]:
    
    temp_LUT = []
    for k_item in Odia_data_3[i]:
        k= k_item.split('*')
        k_str= ''
        for j_item in k:
            j = int (j_item)
            if j >0:
                k_str= k_str + master_Odia_LUT [j-1]
            else:
                k_str = k_str + master_gen_LUT [-j-1]
        temp_LUT.append(k_str)
    Interpreted_LUT  .append(temp_LUT) 

#empasis_exclusion_list = Interpreted_LUT [5]

empasis_exclusion_list = [' ']


# del currentPlace, Odia_data2, temp_LUT, master_gen_LUT, line
# del k_str, k_item, j_item, j, k, i, item, filehandle, 


de_emphasis_arr = [[],[],[],[]]
for j,i in enumerate( Interpreted_LUT [1]):
    if  i in  Interpreted_LUT [2] or i in  Interpreted_LUT [3] or  Interpreted_LUT [2][j] in Interpreted_LUT [4] or Interpreted_LUT [3][j] in Interpreted_LUT [4]:
        empasis_exclusion_list.append(i)
        print ('Warning - EXclusion list for empasis  '+ i , j)
    de_emphasis_arr[0].append(Interpreted_LUT [2][j])
    de_emphasis_arr[1].append(i)
    de_emphasis_arr[2].append(Interpreted_LUT [4][j])
    de_emphasis_arr[3].append(Interpreted_LUT [3][j])



control_based_juktakshar = {}
b= Odia_data_3[10]
for j,i in enumerate(b):
    if not i[0].isalpha():
        i_lists= i.split('*')
        i_str= ''
        for k in i_lists:
            k_num = int (k)
            if k_num>0:
                i_str=i_str + master_Odia_LUT [k_num-1]
            else:
                raise KeyboardInterrupt
        control_based_juktakshar [control_inp_types [j]] = i_str
        

Numbers_map          = dict(zip(Odia_data_3[2], Interpreted_LUT [0]))  # dict(zip(keys, values))
Normal_map           = dict(zip(Odia_data_3[1], Interpreted_LUT [1]))  
Shift_map            = dict(zip(Odia_data_3[0], Interpreted_LUT [3])) 

Emphasis_map         = dict(zip(Interpreted_LUT [1], Interpreted_LUT [2])) 
Shift_Phalasis_map   = dict(zip(Interpreted_LUT[3], Interpreted_LUT [4]))   #Shift_Phalasis_map = single time Phalasis only

Double_Phalasis_map   = dict(zip(Interpreted_LUT [2], Interpreted_LUT [4])) 

de_EmPhalaSis_map   = dict(zip(de_emphasis_arr [0]+de_emphasis_arr [2], de_emphasis_arr[1]+de_emphasis_arr [3])) 
odChr_CanBe_de_EmPhalaSized = de_emphasis_arr [0]+de_emphasis_arr [2]

juktakhar_Phalasis =  dict(zip(Interpreted_LUT[5], Interpreted_LUT [6])) 
# single_EmPhalasis_exclusion_list = Interpreted_LUT[3]

         
empasis_exclusion_list = empasis_exclusion_list+ Odia_data_3[2]# + list (control_based_juktakshar.keys())     
valid_EN_char = Odia_data_3[0]+Odia_data_3[1]+Odia_data_3[2] +   list (control_based_juktakshar.keys())     


characterMap= {**Normal_map, **Numbers_map, **Shift_map , **control_based_juktakshar}
Superset_EmPhalasis_map = {**Emphasis_map,**Shift_Phalasis_map, **Double_Phalasis_map , **juktakhar_Phalasis }


valid_odChr_base_no_EmPhalaSis = Interpreted_LUT [1]+Interpreted_LUT [3] + list(juktakhar_Phalasis.keys()) +Interpreted_LUT [2]
# valid_odChr_EmPhalaSized = Interpreted_LUT [2]

last_EmPhalasis_list = Interpreted_LUT [4]

'''