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
space_emphasis_flag = False

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
    return inp3 in number_result_ord
    # return 48 <= inp3 <= 57 or inp3 == 46
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
    global Disable_Odia_FSM, Disable_Odia_typing, space_emphasis_flag

    chr_pressed = kp
    
    # print (kp, len(eng_stack) , len(main_text_stack), len(h_flag_list),len(f_flag_list) )

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
        if space_emphasis_flag:
            flagH = ascii_num in space_emphasis_list
        else:
            flagH = False
        
        #print (flagA, flagB, flagC, flagD, flagF, Disable_Odia_typing)

        
        if flagA or flagB or flagC or flagD and not (Disable_Odia_typing): 
            to_delete_last = False

            if flagH:
                mode, new_ascii = space_emphasis_map [ascii_num ]
                ascii_num = ord (new_ascii )
                isIt_emphasized_now_h, isIt_emphasized_now_f = False, False
                h_emphasis_flag, f_emphasis_flag = False, False
                eng_char = kp[1]
                # print (mode, ascii_num)
                flagC= False
            elif flagF:
                mode = 4
                to_delete_last = True
                ascii_num = ord ( eng_stack [-2] )      
                eng_char ='-hf-'
                h_emphasis_flag, f_emphasis_flag = False, False
                if ascii_num== ascii_h:
                    isIt_emphasized_now_h, isIt_emphasized_now_f = True, False
                else:
                    isIt_emphasized_now_h, isIt_emphasized_now_f = False, True                  
                
            elif flagA:
                to_delete_last = True
                
                ascii_num = ord ( eng_stack [-1] )
                flagC = isCap (ascii_num)
                flagD = isSmall (ascii_num)
                eng_char =  '-h-'
                isIt_emphasized_now_h, isIt_emphasized_now_f = True, False
                if flagD :
                    mode = 1
                    h_emphasis_flag, f_emphasis_flag = False, True
                elif ascii_num == 32:
                    #print ('Ha char only - faking the input')
                    mode = 0
                    ascii_num = 120
                    isIt_emphasized_now_h, isIt_emphasized_now_f = False, False
                    h_emphasis_flag, f_emphasis_flag = False, False
                    to_delete_last = False
                else: #flagD
                    mode = 5
                    h_emphasis_flag, f_emphasis_flag = False, False
            elif flagB:
                to_delete_last  =True
                
                ascii_num = ord ( eng_stack [-1] )
                flagC = isCap (ascii_num)
                # No capital possible here            
                mode = 2
                eng_char  = '-f-'
                h_emphasis_flag, f_emphasis_flag = True, False
                isIt_emphasized_now_h, isIt_emphasized_now_f = False, True
            elif flagE:
                text_box.config(state="disabled")  
                return    
            elif flagC:
                mode = 3
                h_emphasis_flag , f_emphasis_flag = True, False 
                eng_char = kp[1] 
                isIt_emphasized_now_h, isIt_emphasized_now_f = False, False
                # pass
            elif flagD:
                mode = 0
                h_emphasis_flag, f_emphasis_flag = True, True
                eng_char =kp[1]
                isIt_emphasized_now_h, isIt_emphasized_now_f = False, False
                # pass
            else:
                # text_box.config(state="disabled")   
                # return
                pass #usually won't come
                

            class_index_num = (ascii_num - 65) if flagC else (ascii_num - 97)                

            # print (mode, class_index_num)            
                       
            # print (mode, text_LUT [class_index_num] )
            col = text_LUT [class_index_num]
            if 0 < col <= threshold_class0_end and mode < class0_Column_length :
                pass
            elif threshold_class0_end < col <= threshold_class1_end and mode < class1_Column_length :
                pass
            elif  threshold_class1_end < col <= threshold_class2_end and mode < class2_Column_length:   
                pass 
            elif threshold_class2_end < col <= threshold_class3_end and mode < class3_Column_length:
                pass
            else:
                print ('Invalid character call')
                text_box.config(state="disabled") 
                return
                
            if to_delete_last == True:
                od_uni = main_text_stack [-1]
                last_len= len(od_uni)
                text_box.delete('end-'+str(last_len+1)+'c', 'end-1c')
                
            
            od_uni = get_LUT(mode, text_LUT [class_index_num] )
            text_box.insert(tkinter.END, od_uni )
            main_text_stack.append( od_uni ) 
            h_flag_list .append ([isIt_emphasized_now_h, h_emphasis_flag])
            f_flag_list .append ([isIt_emphasized_now_f, f_emphasis_flag])   
            eng_stack.append(eng_char)
            space_emphasis_flag= False
            
            

        elif kp == "']'":
            print ('copied')
            pyperclip.copy(text_box.get('1.0', tkinter.END))
            #pyperclip.copy(''.join(main_text_stack) )  # Commented out after implementation of ENG switch
            text_box.config(state="disabled")   
            return
        else:
            h_emphasis_flag, f_emphasis_flag = False , False
            h_flag_list .append ([False,False])   
            f_flag_list .append ([False,False])   
            if flagG :
                od_uni = Number_map[kp[1]]
                text_box.insert(tkinter.END, od_uni)                     
            else:
                od_uni = kp[1]
                text_box.insert(tkinter.END, od_uni)
                
            space_emphasis_flag= True
                    # h_emphasis_flag = True                      
            
            eng_stack.append( kp[1] )
            main_text_stack.append( od_uni ) 
            
            
    # return
    # if 1:
    #     pass
    else:
    # if (kp == "'\\t'" or kp == "'['") and  valid_EmPhalasis== True: #space
    #     last_od_ty
        space_emphasis_flag= True
        if kp == "'\\x08'" : # Backspace
            od_uni = main_text_stack.pop()   
            h_emphasis_flag_local = h_flag_list.pop ()
            f_emphasis_flag_local = f_flag_list.pop ()
            en_chr = eng_stack.pop()
                     
            
            space_emphasis_flag= False
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
                eng_stack.append('')
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
            h_emphasis_flag, f_emphasis_flag = False , False
            h_flag_list .append ([False,False])  
            f_flag_list .append ([False,False])  
            
            if kp == "'\\r'":  #Enter
                text_box.insert(tkinter.END, '\n')     
                main_text_stack.append('\n')
                space_emphasis_flag= True
            elif kp == "'\\t'": #"'\\t'" or kp == "']'":  # halant for tab 
                text_box.insert(tkinter.END, chr (2893) )          
                main_text_stack.append(  chr (2893) )
            else:
                eng_stack. pop()
                h_flag_list.pop ()
                f_flag_list.pop()
                text_box.config(state="disabled") 
                return
                    
    # print (len(eng_stack) , len(main_text_stack), len(h_flag_list),len(f_flag_list) )
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

