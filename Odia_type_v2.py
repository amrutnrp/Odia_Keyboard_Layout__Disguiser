# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 02:37:17 2021

@author: amrutnp
"""
import tkinter
root = tkinter.Tk()
from Import_odia_process import  *
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



#=====================================================================================
def key(event):
    kp = repr(event.char)
    if len(kp)==2 or len (kp) == 0 :
        return    
    
    global chr_pressed, valid_emphasis ,last_input, valid_double_emphasis, last_od_type, valid_de_emphasis
    chr_pressed = kp
    
    text_box.config(state="normal")
    #print ("pressed", kp,  len(kp)) #repr(event.char))

    if (kp == "'\\t'" or kp == "']'" ) and  valid_emphasis== True: #space
        last_len= len(last_od_type)
        text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
        od_uni = Superset_empasis_map[last_od_type]            
        od_chr = repr(od_uni)
        text_box.insert(tkinter.END, od_chr [1:-1])       
        valid_emphasis = False  
        if last_od_type in single_emphasis_exclusion_list:
            valid_double_emphasis= False
        else:
            valid_double_emphasis= True
        valid_de_emphasis = True       
    elif (kp == "'\\t'" or kp == "']'" ) and valid_double_emphasis== True:  # double space
        last_len= len(last_od_type)
        text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
        od_uni = Double_Emphasis_map[last_od_type]            
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
        valid_de_emphasis = False
        valid_double_emphasis= False
        if kp in empasis_exclusion_list :
            valid_emphasis = False
        else:
            valid_emphasis = True
    else:
        valid_emphasis = False
        valid_double_emphasis= False        
        if len (kp) == 3:
            text_box.insert(tkinter.END, kp[1])
            valid_de_emphasis = False
        else:
            if kp == "'\\x08'" : # Backspace
                last_od_type = text_box.get('end-2c', 'end-1c')
                if valid_de_emphasis and last_od_type in valid_od_char_deEmpasized:
                    text_box.delete('end-2c', 'end-1c')
                    od_uni = De_Emphasis_map[last_od_type]
                    od_chr = repr(od_uni)
                    last_od_type = od_chr[1:-1]
                    text_box.insert(tkinter.END,last_od_type  )
                else:
                    text_box.delete('end-2c', 'end-1c')
                    last_od_type = text_box.get('end-2c', 'end-1c')
                if last_od_type in valid_od_char:
                    valid_emphasis = True
                    valid_double_emphasis= False
                elif last_od_type in valid_od_char_empasized:
                    valid_emphasis = False
                    valid_double_emphasis= True
            elif kp == "'\\r'":  #Enter
                text_box.insert(tkinter.END, '\n')        
                valid_de_emphasis = False
            elif kp == "' '":  #space
                text_box.insert(tkinter.END, '\n')        
                valid_de_emphasis = False                
            else:
                valid_de_emphasis = False
    text_box.config(state="disabled")   
    
characterMap= {**Normal_map, **Numbers_map, **Shift_map , **control_based_juktakshar}
Superset_empasis_map = {**Emphasis_map,**Shift_Emphasis_map , **juktakhar_emphasis }

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

