# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:41:41 2021

@author: amrut
"""
import pyperclip
import tkinter
root = tkinter.Tk()
from Import_odia_process_2  import  *

print('Programm starting...')

chr_pressed =None

h_emphasis_flag = False
f_emphasis_flag = False

main_text_stack = ['']
eng_stack = ['']
h_flag_list =[[False, False]]
f_flag_list =[[False, False]]


Disable_Odia_typing = False
Disable_Odia_FSM = 0

def isCap (inp1):
    return 65 <= inp1 <= 90
def isSmall (inp2):
    return 97 <= inp2 <= 122
def isNUmDOT (inp3):
    return 48 <= inp3 <= 57 or inp3 == 46
ascii_h = 104
ascii_f = 102
ascii_H = 70
ascii_F = 72
fh_l = [70,72,102,104]
#=====================================================================================
def key(event):
    kp = repr(event.char)   
    if len(kp)==2 or len (kp) == 0 :
        return
    global  chr_pressed
    global  h_emphasis_flag,f_emphasis_flag
    global eng_stack, main_text_stack, h_flag_list, f_flag_list
    global Disable_Odia_FSM, Disable_Odia_typing

    chr_pressed = kp
    
    print (eng_stack )

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
        if kp == "'-'":
            text_box.delete('1.0', tkinter.END)
            Disable_Odia_typing= True
            kp = "' '"
            Disable_Odia_FSM = 3
        

    if len (kp) == 3:
        ascii_num = ord (kp[1])
        
        
        flagA = (ascii_num== ascii_h and h_emphasis_flag ) # h emphasis 
        flagB = (ascii_num== ascii_f and f_emphasis_flag ) # f emphasis 
        flagC = isCap (ascii_num)
        flagD = isSmall(ascii_num)
        flagF = (h_flag_list [-1][0] and ascii_num== ascii_f ) or (f_flag_list[-1][0] and ascii_num== ascii_h )
        flagE = (ascii_num in fh_l )     
        flagG = isNUmDOT (ascii_num)
        
        print (flagA, flagB, flagC, flagD, flagF)

        
        if flagA or flagB or flagC or flagD: 

            if flagF:
                mode = 4
                od_uni = main_text_stack [-1]
                last_len= len(od_uni)
                text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
                
                ascii_num = ord ( eng_stack [-2] )      
                eng_stack.append('-hf-')
                h_emphasis_flag, f_emphasis_flag = False, False
                if ascii_num== ascii_h:
                    h_flag_list .append ([True, h_emphasis_flag])
                    f_flag_list .append ([False, f_emphasis_flag]) 
                else:
                    h_flag_list .append ([False, h_emphasis_flag])
                    f_flag_list .append ([True, f_emphasis_flag]) 
                      
                
            elif flagA:
                od_uni = main_text_stack [-1]
                last_len= len(od_uni)
                text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
                
                ascii_num = ord ( eng_stack [-1] )
                eng_stack.append( '-h-')
                
                if flagD :
                    mode = 1
                    h_emphasis_flag, f_emphasis_flag = False, True
                    h_flag_list .append ([True, h_emphasis_flag])
                    f_flag_list .append ([False, f_emphasis_flag])                  
                else: #flagD
                    mode = 5
                    h_emphasis_flag, f_emphasis_flag = False, False
                    h_flag_list .append ([True, h_emphasis_flag])
                    f_flag_list .append ([False, f_emphasis_flag])                       
            elif flagB:
                od_uni = main_text_stack [-1]
                last_len= len(od_uni)
                text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
                
                ascii_num = ord ( eng_stack [-1] )
                
                        
                # No capital possible here            
                mode = 2
                eng_stack.append('-f-')
                h_emphasis_flag, f_emphasis_flag = True, False
                h_flag_list .append ([False, h_emphasis_flag])
                f_flag_list .append ([True, f_emphasis_flag])  
            elif flagE:
                text_box.config(state="disabled")  
                return    
            elif flagC:
                mode = 3
                h_emphasis_flag , f_emphasis_flag = True, False 
                eng_stack.append(kp[1] )
                h_flag_list .append ([False, h_emphasis_flag])
                f_flag_list .append ([False, f_emphasis_flag])  
                # pass
            elif flagD:
                mode = 0
                h_emphasis_flag, f_emphasis_flag = True, True
                eng_stack.append(kp[1] )
                h_flag_list .append ([False, h_emphasis_flag])
                f_flag_list .append ([False, f_emphasis_flag])  
                # pass
            else:
                # text_box.config(state="disabled")   
                # return
                pass #usually won't come
                

            class_index_num = (ascii_num - 65) if flagC else (ascii_num - 97)                

            print (mode, class_index_num)            
                       
            print (mode, text_LUT [class_index_num] )
            od_uni = get_LUT(mode, text_LUT [class_index_num] )
            text_box.insert(tkinter.END, od_uni )
            main_text_stack.append( od_uni ) 
            
            
            

        elif kp == "']'":
            pyperclip.copy(text_box.get('1.0', tkinter.END))
            #pyperclip.copy(''.join(main_text_stack) )  # Commented out after implementation of ENG switch
            text_box.config(state="disabled")   
            return
        else:
            if flagG :
                od_uni = Number_map[kp[1]]
                text_box.insert(tkinter.END, od_uni )
            else:
                od_uni = kp[1]
                text_box.insert(tkinter.END, od_uni)
            
            h_flag_list .append ([False,False])   
            f_flag_list .append ([False,False])   
            eng_stack.append( kp[1] )
            h_emphasis_flag, f_emphasis_flag = False , False
            main_text_stack.append( od_uni ) 
            
            
    # return
    # if 1:
    #     pass
    else:
    # if (kp == "'\\t'" or kp == "'['") and  valid_EmPhalasis== True: #space
    #     last_od_ty
        if kp == "'\\x08'" : # Backspace
            od_uni = main_text_stack.pop()   
            h_emphasis_flag_local = h_flag_list.pop ()
            f_emphasis_flag_local = f_flag_list.pop ()
            en_chr = eng_stack.pop()
                     
            if Disable_Odia_typing :
                text_box.delete('end-2c', 'end-1c')
            else:
                last_len= len(od_uni)
                text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
                if h_emphasis_flag_local [0] or f_emphasis_flag_local [0]:
                    text_box.insert(tkinter.END,main_text_stack [-1] )
                                  
                    
                h_emphasis_flag = h_flag_list [-1] [1]
                f_emphasis_flag = f_flag_list [-1] [1]
                        
                        
            if len(main_text_stack) <= 1:
                main_text_stack.append('')
            if len(h_flag_list) <= 1:
                h_flag_list.append([False,False])
            if len(f_flag_list) <= 1:
                f_flag_list.append([False,False])                
            if len(eng_stack) <= 1:
                eng_stack.append(False)
            text_box.config(state="disabled")   
            return
        elif kp in special_symbols:
            od_uni = Dict_special_symbol_map[kp] 
            text_box.insert(tkinter.END, od_uni )
            
            h_emphasis_flag, f_emphasis_flag = False , False
            
            main_text_stack .append( od_uni )
            eng_stack.append( kp )
            h_flag_list .append ([False,False]) 
            f_flag_list.append ([False,False]) 
            
        else:
            eng_stack.append( kp )
            h_flag_list .append ([False,False])             
            if kp == "'\\r'":  #Enter
                text_box.insert(tkinter.END, '\n')     
                main_text_stack.append('\n')
            elif kp == "' '": #"'\\t'" or kp == "']'":  #space
                text_box.insert(tkinter.END, ' ')          
                main_text_stack.append(' ')
            elif kp == "'\\t'": #"'\\t'" or kp == "']'":  #space
                text_box.insert(tkinter.END, chr (2893) )          
                main_text_stack.append(  chr (2893) )
            else:
                eng_stack. pop()
                h_flag_list.pop ()
                text_box.config(state="disabled") 
                return
                    
    print (eng_stack )#, main_text_stack, h_flag_list)
    text_box.config(state="disabled")   
    if Disable_Odia_typing :
        #text_box.insert(tkinter.END, repr((kp)))
        #text_box.config(state="disabled")
        main_text_stack = ['']
        eng_stack = ['']
        h_emphasis_flag, f_emphasis_flag = False , False
        h_flag_list, f_flag_list =[[False, False]], [[False, False]]
        
        if Disable_Odia_FSM == 3:
            Disable_Odia_FSM =0
            Disable_Odia_typing = False
        return
    


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

