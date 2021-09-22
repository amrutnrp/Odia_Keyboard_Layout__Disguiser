# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 02:37:17 2021

@author: amrutnp
"""
import pyperclip
import tkinter
root = tkinter.Tk()
from Import_odia_process import  de_EmPhalaSis_map, empasis_exclusion_list , valid_EN_char, valid_odChr_base_no_EmPhalaSis, odChr_CanBe_de_EmPhalaSized, characterMap, Superset_EmPhalasis_map, last_EmPhalasis_list
#single_EmPhalasis_exclusion_list

print('Programm starting...')
chr_pressed =None
# flag=0
#import re
#main_string = ""
valid_EmPhalasis = False
last_od_type = '%'
valid_de_EmPhalasis = False
main_text_stack = ['']
last_char_flag = [False]
de_emph_vld_flag_arr=  [False]
Disable_Odia_typing = False
Disable_Odia_FSM = 0
#=====================================================================================
def key(event):
    kp = repr(event.char)
    if len(kp)==2 or len (kp) == 0 :
        return
    global Disable_Odia_FSM, Disable_Odia_typing
    global chr_pressed, valid_EmPhalasis
    global last_char_flag, main_text_stack
    global  last_od_type
    global valid_de_EmPhalasis, de_emph_vld_flag_arr
    chr_pressed = kp

    text_box.config(state="normal")
    if kp == "'`'":
        if Disable_Odia_FSM ==0:
            Disable_Odia_FSM = 1
        else:# Disable_Odia_FSM ==1:
            Disable_Odia_typing = not (Disable_Odia_typing )
            Disable_Odia_FSM = 0
            text_box.delete('end-2c', 'end-1c')
            text_box.config(state="disabled")
            return
    elif Disable_Odia_FSM == 1 :
        Disable_Odia_FSM = 0
        
    #print ("pressed", kp,  len(kp)) #repr(event.char))
    #print (len(de_emph_vld_flag_arr),len(last_char_flag),len(main_text_stack), main_text_stack ) 
    if (kp == "'\\t'" or kp == "'['") and  valid_EmPhalasis== True: #space
        last_od_type = main_text_stack[-1]   
        last_len= len(last_od_type)
        text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
        od_uni = Superset_EmPhalasis_map[last_od_type]            
        text_box.insert(tkinter.END, od_uni)   
        main_text_stack[-1] = od_uni
        if od_uni in last_EmPhalasis_list:
            valid_EmPhalasis= False
        else:
            valid_EmPhalasis= True
        valid_de_EmPhalasis = True     
        de_emph_vld_flag_arr.pop()
    elif not (Disable_Odia_typing) and kp in valid_EN_char :
        od_uni = characterMap[kp]
        text_box.insert(tkinter.END, od_uni )
        main_text_stack.append( od_uni )
        last_char_flag.append(True)
        valid_de_EmPhalasis = False
        if kp in empasis_exclusion_list :
            valid_EmPhalasis = False
        else:
            valid_EmPhalasis = True
    elif kp == "'\\x08'" : # Backspace
        valid_de_EmPhalasis = de_emph_vld_flag_arr.pop()
        back_odia_chr_check = last_char_flag.pop()
        last_od_type = main_text_stack.pop() #text_box.get('end-2c', 'end-1c')
        # print (de_emph_vld_flag_arr , last_char_flag, main_text_stack)
        
        
        if Disable_Odia_typing :
            text_box.delete('end-2c', 'end-1c')
        else:
            last_len= len(last_od_type)
            text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
        
            if back_odia_chr_check and valid_de_EmPhalasis:
                if last_od_type in odChr_CanBe_de_EmPhalaSized:
                    last_od_type = de_EmPhalaSis_map[last_od_type]
                    text_box.insert(tkinter.END,last_od_type  )
                    main_text_stack.append(last_od_type)
                    last_char_flag.append(True)
                    
                    if last_od_type in valid_odChr_base_no_EmPhalaSis:
                        valid_EmPhalasis = True
                    else:
                        valid_EmPhalasis= False
                    de_emph_vld_flag_arr.append(valid_de_EmPhalasis)
        if len(main_text_stack) <= 1:
            main_text_stack.append('')
        if len(de_emph_vld_flag_arr) <= 1:
            de_emph_vld_flag_arr.append(False)
        if len(last_char_flag) <= 1:
            last_char_flag.append(False)
        text_box.config(state="disabled")   
        return            
    else:
        valid_EmPhalasis = False
        valid_de_EmPhalasis = False
        last_char_flag.append(False)
        if len (kp) == 3:
            if kp == "']'":
                last_char_flag.pop()
                pyperclip.copy(text_box.get('1.0', tkinter.END))
                #pyperclip.copy(''.join(main_text_stack) )  # Commented out after implementation of ENG switch
                text_box.config(state="disabled")   
                return
            elif kp == "'['" :
                text_box.insert(tkinter.END, ' ')          
                main_text_stack.append(' ')                
                # text_box.config(state="disabled")  
                # return
            else:
                text_box.insert(tkinter.END, kp[1])
                main_text_stack.append(kp[1])
        else:
            if kp == "'\\r'":  #Enter
                text_box.insert(tkinter.END, '\n')     
                main_text_stack.append('\n')
            elif kp == "' '": #"'\\t'" or kp == "']'":  #space
                text_box.insert(tkinter.END, ' ')          
                main_text_stack.append(' ')
            else: 
                last_char_flag.pop()
                text_box.config(state="disabled") 
                return
    text_box.config(state="disabled")   
    if Disable_Odia_typing :
        #text_box.insert(tkinter.END, repr((kp)))
        #text_box.config(state="disabled")
        valid_EmPhalasis = False
        last_od_type = '%'
        valid_de_EmPhalasis = False
        main_text_stack = ['']
        last_char_flag = [False]
        de_emph_vld_flag_arr=  [False]
        return
    de_emph_vld_flag_arr.append(valid_de_EmPhalasis)
    


def callback(event):
    text_box.focus_set()
    #print ("clicked at", event.x, event.y)
text_box = tkinter.Text(root, width =40, height = 20 ,  font=("Helvetica", 16))
#text_box.insert("1.0", sample_text)
text_box.bind("<Key>", key)
text_box.bind("<Button-1>", callback)
text_box.config(state="disabled")
text_box.pack()
root.mainloop()

