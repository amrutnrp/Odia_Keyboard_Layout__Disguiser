# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 02:37:17 2021

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
        
for i in [4,5,6,7,8, 10,11,12,13]:
    
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
empasis_exclusion_list = [' ', '-']
valid_EN_char = Odia_data_3[0]+Odia_data_3[1]+Odia_data_3[2]
valid_od_char = Interpreted_LUT [1]+Interpreted_LUT [2]+Interpreted_LUT [3]
valid_od_char_empasized = Interpreted_LUT [3]
valid_od_char_deEmpasized = Interpreted_LUT [5]+Interpreted_LUT [7]
del currentPlace, Odia_data2, temp_LUT, master_gen_LUT, master_Odia_LUT, line
del k_str, k_item, j_item, j, k, i, item, filehandle, 
Numbers_map          = dict(zip(Odia_data_3[2], Interpreted_LUT [0]))  # dict(zip(keys, values))
Normal_map           = dict(zip(Odia_data_3[1], Interpreted_LUT [1]))  
Shift_map            = dict(zip(Odia_data_3[0], Interpreted_LUT [3])) 

Emphasis_map         = dict(zip(Interpreted_LUT [1], Interpreted_LUT [2])) 
Matra_Emphasis_map   = dict(zip(Interpreted_LUT [2], Interpreted_LUT [4])) 
Shift_Emphasis_map   = dict(zip(Interpreted_LUT[3], Interpreted_LUT [4])) 

De_Emphasis_map   = dict(zip(Interpreted_LUT [5]+Interpreted_LUT [7], Interpreted_LUT[6]+Interpreted_LUT [8])) 



#del Interpreted_LUT, Odia_data_3

from tkinter import *
import tkinter
root = tkinter.Tk()
print('Programm starting...')
chr_pressed =None
flag=0
#import re
#main_string = ""
valid_emphasis = False
valid_double_emphasis= False
last_input = ''
last_od_type = ''
valid_de_emphasis = False



#=====================================================================================
def key(event):
    kp = repr(event.char)
    if len(kp)==2 :
        return    
    
    global chr_pressed
    chr_pressed = kp
    global valid_emphasis ,last_input, valid_double_emphasis, last_od_type, valid_de_emphasis
    
    text_box.config(state="normal")
    #print ("pressed", kp,  len(kp)) #repr(event.char))

    if kp == "' '" and  valid_emphasis== True: #space
        last_len= len(last_od_type)
        text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
        
        print (last_od_type, len(last_od_type))
        
        od_uni = Superset_empasis_map[last_od_type]            
        od_chr = repr(od_uni)
        text_box.insert(tkinter.END, od_chr [1:-1])
        
        valid_emphasis = False  
        valid_double_emphasis= True
        valid_de_emphasis = True
        
    elif kp == "' '" and valid_double_emphasis== True:  # double space
        last_len= len(last_od_type)
        text_box.delete('end-'+str(last_len)+'c', 'end-1c')
        
        od_uni = Superset_empasis_map[last_od_type]            
        od_chr = repr(od_uni)
        text_box.insert(tkinter.END, od_chr [1:-1])
                
        valid_emphasis = False  
        valid_double_emphasis= False
        valid_de_emphasis= True
                
            
            
    elif kp in valid_EN_char :
        od_uni = characterMap[kp]
        od_chr = repr(od_uni)
        last_od_type= od_chr[1:-1]
        text_box.insert(tkinter.END, last_od_type )
        last_input= kp
        
        #print (last_od_type, len(last_od_type))
        valid_de_emphasis = False
        if kp in empasis_exclusion_list :
            valid_emphasis = False
        else:
            valid_emphasis = True
    else:
        valid_emphasis = False
        if len (kp) == 3:
            text_box.insert(tkinter.END, kp[1])
        else:
            if kp == "'\\x08'" : # Backspace
                last_od_type = text_box.get('end-2c', 'end-1c')
                if last_od_type in valid_od_char_deEmpasized:
                    print ('hmm - ', last_od_type)
                    text_box.delete('end-2c', 'end-1c')
                    od_uni = De_Emphasis_map[last_od_type]
                    od_chr = repr(od_uni)
                    text_box.insert(tkinter.END, od_chr[1:-1] )
                    
                    
                    
                else:
                        
                    text_box.delete('end-2c', 'end-1c')
                    last_od_type = text_box.get('end-2c', 'end-1c')
                    if last_od_type in valid_od_char:
                        valid_emphasis = True
                        valid_double_emphasis= False
                    elif last_od_type in valid_od_char_empasized:
                        valid_emphasis = False
                        valid_double_emphasis= True
                    #last_type= '\''+last_type+ '\''

            elif kp == "'\\r'":  #Enter
                text_box.insert(tkinter.END, '\n')        
                valid_de_emphasis = False
            else:
                valid_de_emphasis = False
    text_box.config(state="disabled")
    
    
characterMap= {**Normal_map, **Numbers_map, **Shift_map }
Superset_empasis_map = {**Emphasis_map,**Shift_Emphasis_map , **Matra_Emphasis_map }

#valid_od_char = list(characterMap.keys() )

def callback(event):
    text_box.focus_set()
    #print ("clicked at", event.x, event.y)
text_box = tkinter.Text(root, width =30, height = 10 ,  font=("Helvetica", 32))
#text_box.insert("1.0", sample_text)
text_box.bind("<Key>", key)
text_box.bind("<Button-1>", callback)
text_box.config(state="disabled")
text_box.pack()
root.mainloop()

