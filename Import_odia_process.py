# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:16:26 2021

@author: amrut
"""

Odia_data2 = []

# open file and read the content in a list
with open('Odia_data.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        Odia_data2.append(currentPlace)
        
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
        
for i in [4,5,6,7,8, 10,11,12,13, 15, 16]:
    
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
valid_od_char = Interpreted_LUT [1]+Interpreted_LUT [2]+Interpreted_LUT [3]
valid_od_char_empasized = Interpreted_LUT [3]

del currentPlace, Odia_data2, temp_LUT, master_gen_LUT, line
del k_str, k_item, j_item, j, k, i, item, filehandle, 


emp_arr = [[],[],[],[]]
for j,i in enumerate( Interpreted_LUT [1]):
    if  i in  Interpreted_LUT [2] or i in  Interpreted_LUT [3] or  Interpreted_LUT [2][j] in Interpreted_LUT [4] or Interpreted_LUT [3][j] in Interpreted_LUT [4]:
        empasis_exclusion_list.append(i)
        print ('Warning - EXclusion list for empasis  '+ i , j)
    emp_arr[0].append(Interpreted_LUT [2][j])
    emp_arr[1].append(i)
    emp_arr[2].append(Interpreted_LUT [4][j])
    emp_arr[3].append(Interpreted_LUT [3][j])


Numbers_map          = dict(zip(Odia_data_3[2], Interpreted_LUT [0]))  # dict(zip(keys, values))
Normal_map           = dict(zip(Odia_data_3[1], Interpreted_LUT [1]))  
Shift_map            = dict(zip(Odia_data_3[0], Interpreted_LUT [3])) 

Emphasis_map         = dict(zip(Interpreted_LUT [1], Interpreted_LUT [2])) 
Shift_Emphasis_map   = dict(zip(Interpreted_LUT[3], Interpreted_LUT [4]))   #Shift_Emphasis_map = single time emphasis only

Double_Emphasis_map   = dict(zip(Interpreted_LUT [1], Interpreted_LUT [4])) 

De_Emphasis_map   = dict(zip(emp_arr [0]+emp_arr [2], emp_arr[1]+emp_arr [3])) 
valid_od_char_deEmpasized = emp_arr [0]+emp_arr [2]

juktakhar_emphasis =  dict(zip(Interpreted_LUT[9], Interpreted_LUT [10])) 
single_emphasis_exclusion_list = Interpreted_LUT[3]

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

control_based_juktakshar = {}
b= Odia_data_3[14]
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
         
empasis_exclusion_list = empasis_exclusion_list+ Odia_data_3[2]# + list (control_based_juktakshar.keys())     
valid_EN_char = Odia_data_3[0]+Odia_data_3[1]+Odia_data_3[2] +   list (control_based_juktakshar.keys())     
#del Interpreted_LUT, Odia_data_3    , master_Odia_LUT    
#from tkinter import *
