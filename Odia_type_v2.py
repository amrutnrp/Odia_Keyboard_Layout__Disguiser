# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 02:37:17 2021

@author: amrutnp
"""
import pyperclip
import tkinter
root = tkinter.Tk()
from Import_odia_process import De_Emphasis_map,Double_Emphasis_map, empasis_exclusion_list  , single_emphasis_exclusion_list, valid_EN_char, valid_od_char, valid_od_char_deEmpasized, valid_od_char_empasized,characterMap, Superset_empasis_map

print('Programm starting...')
chr_pressed =None
flag=0
#import re
#main_string = ""
valid_emphasis = False
valid_double_emphasis= False
last_input = ''
last_od_type = '%'
valid_de_emphasis = False
main_text_stack = ['']
last_char_flag = [False]
de_emph_vld_flag_arr=  [False]
#=====================================================================================
def key(event):
    kp = repr(event.char)
    if len(kp)==2 or len (kp) == 0 :
        return    
    
    global chr_pressed, valid_emphasis ,last_input
    global last_char_flag, main_text_stack
    global valid_double_emphasis, last_od_type
    global valid_de_emphasis, de_emph_vld_flag_arr
    chr_pressed = kp
    
    text_box.config(state="normal")
    #print ("pressed", kp,  len(kp)) #repr(event.char))
    print (len(de_emph_vld_flag_arr),len(last_char_flag),len(main_text_stack), main_text_stack ) 
    if (kp == "'\\t'" or kp == "']'" ) and  valid_emphasis== True: #space
        last_od_type = main_text_stack.pop()    
        last_len= len(last_od_type)
        text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
        od_uni = Superset_empasis_map[last_od_type]            
        od_chr = repr(od_uni)
        text_box.insert(tkinter.END, od_chr [1:-1])   
        main_text_stack.append(od_chr [1:-1])
        valid_emphasis = False  
        if last_od_type in single_emphasis_exclusion_list:
            valid_double_emphasis= False
        else:
            valid_double_emphasis= True
        valid_de_emphasis = True     
        de_emph_vld_flag_arr.pop()
    elif (kp == "'\\t'" or kp == "']'" ) and valid_double_emphasis== True:  # double space
        last_len= len(main_text_stack.pop())
        text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
        od_uni = Double_Emphasis_map[last_od_type]            
        od_chr = repr(od_uni)
        text_box.insert(tkinter.END, od_chr [1:-1])
        main_text_stack.append(od_chr [1:-1])
        valid_emphasis = False  
        valid_double_emphasis= False
        valid_de_emphasis= True
        de_emph_vld_flag_arr.pop()
    elif kp in valid_EN_char :
        od_uni = characterMap[kp]
        od_chr = repr(od_uni)
        last_od_type= od_chr[1:-1]
        text_box.insert(tkinter.END, last_od_type )
        main_text_stack.append( last_od_type )
        last_input= kp
        last_char_flag.append(True)
        valid_de_emphasis = False
        valid_double_emphasis= False
        if kp in empasis_exclusion_list :
            valid_emphasis = False
        else:
            valid_emphasis = True
    elif kp == "'\\x08'" : # Backspace
        valid_de_emphasis = de_emph_vld_flag_arr.pop()
        back_odia_chr_check = last_char_flag.pop()
        last_od_type = main_text_stack.pop() #text_box.get('end-2c', 'end-1c')
        # print (de_emph_vld_flag_arr , last_char_flag, main_text_stack)
        
        last_len= len(last_od_type)
        text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
        
        if back_odia_chr_check and valid_de_emphasis:
            if last_od_type in valid_od_char_deEmpasized:
                od_uni = De_Emphasis_map[last_od_type]
                od_chr = repr(od_uni)
                last_od_type = od_chr[1:-1]
                text_box.insert(tkinter.END,last_od_type  )
                main_text_stack.append(last_od_type)
                last_char_flag.append(True)
            
                last_od_type = main_text_stack[-1] 
                if last_od_type in valid_od_char:
                    valid_emphasis = True
                    valid_double_emphasis= False
                elif last_od_type in valid_od_char_empasized:
                    valid_emphasis = False
                    valid_double_emphasis= True
                else:
                    valid_emphasis, valid_double_emphasis = False, False
                de_emph_vld_flag_arr.append(valid_de_emphasis)
        if len(main_text_stack) == 1:
            main_text_stack.append('')
        if len(de_emph_vld_flag_arr) == 1:
            de_emph_vld_flag_arr.append(False)
        if len(last_char_flag) == 1:
            last_char_flag.append(False)
        text_box.config(state="disabled")   
        return            
    else:
        valid_emphasis = False
        valid_double_emphasis= False 
        valid_de_emphasis = False
        last_char_flag.append(False)
        if len (kp) == 3:
            if kp == "'['":
                last_char_flag.pop()
                #pyperclip.copy(text_box.get('1.0', tkinter.END))
                pyperclip.copy(''.join(main_text_stack) )
                text_box.config(state="disabled")   
                return
            elif kp == "']'" :
                text_box.config(state="disabled")  
                return
            else:
                text_box.insert(tkinter.END, kp[1])
                main_text_stack.append(kp[1])
        else:
            if kp == "'\\r'":  #Enter
                text_box.insert(tkinter.END, '\n')     
                main_text_stack.append('\n')
            elif kp == "' '":  #space
                text_box.insert(tkinter.END, ' ')          
                main_text_stack.append(' ')
            else: 
                last_char_flag.pop()
                text_box.config(state="disabled") 
                return
    de_emph_vld_flag_arr.append(valid_de_emphasis)
    text_box.config(state="disabled")   
    


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

