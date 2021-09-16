from tkinter import *
from time import  time
root = Tk()
print('Programm starting...')
chr_pressed =None
flag=0
#import re
#main_string = ""
Waiting_for_next_char_flag = False
waiting_for_which_option = ''





#=====================================================================================
def key(event):
    kp = repr(event.char)
    if len(kp)==2 :
        return    
    print ("pressed", kp,  len(kp), event.char) #repr(event.char))
    global chr_pressed
    chr_pressed = kp
    global Waiting_for_next_char_flag ,waiting_for_which_option
    
    text_box.config(state="normal")
    if Waiting_for_next_char_flag == False:
        if kp in valid_od_char :
            od_uni = characterMap[kp]
            od_chr = repr(od_uni)
            text_box.insert(END, od_chr [1:-1])
        elif kp in dependent_char_char:
            Waiting_for_next_char_flag  =True
            waiting_for_which_option = kp
    elif Waiting_for_next_char_flag == True:
        if kp in Second_entry:
            od_uni = next_map[waiting_for_which_option][kp]
            od_chr = repr(od_uni)
            text_box.insert(END, od_chr [1:-1])
        Waiting_for_next_char_flag  =False
    else:
        if len (kp) == 3:
            text_box.insert(END, kp[1])
        else:
            print ('other char')
            #text_box.insert(END, kp[1:-1])
        
    if kp == "'sdgfl'" :
        print (text_box.get('1.0', 'end-1c') )

        od_uni = characterMap[kp]
        repr("\u0B24")

        




    if kp == "' '": #space
        text_box.insert(END, ' ')
    if kp == "'\\r'":  #Enter
        text_box.insert(END, '\n')
    if kp == "'\\x08'" : # Backspace
        text_box.delete('end-2c', 'end-1c')
    text_box.config(state="disabled")


#===================end of funciton===================
characterMap= {
"'A'":"\u0B06",
"'B'":'\u0B26',
"'C'":'\u0B1B',
"'D'":'\u0B22',
"'E'":"\u0B10",
##"'F'":  
"'G'":'\u0B18',
"'H'":'\u0B20',
"'I'":"\u0B08",
"'J'":'\u0B1D',
"'K'":'\u0B16',
"'L'":'\u0B33',
"'M'":'\u0B4D\u0B2E', # \ma
"'N'":'\u0B23',
"'O'":'\u0B14',
"'P'":'\u0B2B',
"'Q'":'\u0964',
"'R'":"\u0B0B",
##"'S'":
##"'T'":
"'U'":"\u0B0A",
"'V'":'\u0B27',
"'W'":'\u0B35',
"'X'":'\u0B39',
"'Y'":'\u0B2F',
"'Z'":'\u0B37',
  
"'a'":"\u0B05",
"'b'":'\u0B2C',
"'c'":'\u0B1A',
"'d'":'\u0B21',
"'e'":"\u0B0F",
"'f'":'\u0B24',
"'g'":'\u0B17',
"'h'":'\u0B25',
"'i'":"\u0B07",
"'j'":'\u0B1C',
"'k'":'\u0B15',
"'l'":'\u0B32',
"'m'":'\u0B2E',
"'n'":'\u0B28',
"'o'":'\u0B13',
"'p'":'\u0B2A',
"'q'":'\u0B4D',
"'r'":'\u0B30',
"'s'":'\u0B38',
"'t'":'\u0B1F',
"'u'":"\u0B09",
"'v'":'\u0B2D',
"'w'":'\u0B71',
"'x'":"\u0B15\u0B4D\u0B37",
"'y'":'\u0B5F',
"'z'":'\u0B36',

"'\\x01'":"\u0B3E",                     #A aa
"'\\x02'":'\u0B4D\u0B2C',       #B /ba
"'\\x03'":'\u0B4D\u0B1A',       #C /cha
"'\\x04'":'\u0B4D\u0B21',       #D /dda
"'\\x05'":"\u0B47",                     #E ae
"'\\x06'":'\u0B4D\u0B24',       #F /ta
"'\\x07'":'\u0B4D\u0B17',       #G  /ga
##"'\\x08'":'\u0B4D\u0B25',                         #H
"'\\t'"  :"\u0B3F",                       #I ii
"'\\n'"  :'\u0B4D\u0B1C',         #J  /ja
"'\\x0b'":'\u0B4D\u0B15',       #K  /ka
"'\\x0c'":'\u0B4D\u0B32',       #L  /la
##'\\r'"   : '\u0B4D\u0B2E',                            #M
"'\\x0e'":'\u0B4D\u0B28',       #N /na
"'\\x0f'":'\u0B4B',                     #O  oh
"'\\x10'":'\u0B4D\u0B2A',       #P /pa
"'\\x11'":'\u0B4D',                     #Q  halant
"'\\x12'":"\u0B4D\u0B30",       #R /ra
"'\\x13'":'\u0B4D\u0B38',                           #S  ??
"'\\x14'":'\u0B4D\u0B1F' ,      #T /ta
"'\\x15'":"\u0B41",                     #U  ou
"'\\x16'":'\u0B4D\u0B2D',       #V /bha
"'\\x17'":'',                                       #W /
"'\\x18'":'',                                       #X  /gyna
"'\\x19'":'\u0B4D\u0B5F',       #Y /ya
"'\\x1a'":'\u0B4D\u0B36',        #Z /sha


"'0'":'\u0B66',
"'1'":'\u0B67',
"'2'":'\u0B68',
"'3'":'\u0B69',
"'4'":'\u0B6A',
"'5'":'\u0B6B',
"'6'":'\u0B6C',
"'7'":'\u0B6D',
"'8'":'\u0B6E',
"'9'":'\u0B6F',
    }        

"""
0B0C
0B19
0B1E

0B3C
0B3D

0B40
0B42
0B43
0B48
0B57

0B44
0B55

"""



next_map =  {
    "'F'":  {           #Brace for (control + Char )+ shift    
        "'A'":"\u0B3E",
        "'B'":'\u0B4D\u0B26',
        "'C'":'\u0B4D\u0B1B',
        "'D'":'\u0B4D\u0B22',
        "'E'":"\0B48",   #\ ai
        "'F'":  '', ##
        "'G'":'\u0B4D\u0B18',
        "'H'":'\u0B4D\u0B20',
        "'I'":"\u0B40",   #\ee
        "'J'":'\u0B4D\u0B1D',
        "'K'":'\u0B4D\0B16',
        "'L'":'\u0B4D\u0B33',
        "'M'":'\u0B4D\u0B2E', # \ma
        "'N'":'\u0B4D\u0B23',
        "'O'":'\u0B57',   #\au
        "'P'":'\u0B4D\u0B2B',
        "'Q'":'',##
        "'R'":"\u0B43",
        "'S'": '',##
        "'T'": '',##
        "'U'":"\u0B42",
        "'V'":'\u0B4D\u0B27',
        "'W'":'\u0B4D\u0B71',
        "'X'":'\u0B03',  #/h
        "'Y'":'\u0B2F\u0B4D\u0B5F', 
        "'Z'":'\u0B4D\u0B37',

        "'a'":"\u0B3E",
        "'b'":'\u0B4D\u0B26',
        "'c'":'\u0B4D\u0B1B',
        "'d'":'\u0B4D\u0B22',
        "'e'":"\0B48",   #\ ai
        "'f'":  '', ##
        "'g'":'\u0B4D\u0B18',
        "'h'":'\u0B4D\u0B20',
        "'i'":"\u0B40",   #\ee
        "'j'":'\u0B4D\u0B1D',
        "'k'":'\u0B4D\0B16',
        "'l'":'\u0B4D\u0B33',
        "'M'":'\u0B4D\u0B2E', # \ma
        "'n'":'\u0B4D\u0B23',
        "'o'":'\u0B57',   #\au
        "'p'":'\u0B4D\u0B2B',
        "'q'":'',##
        "'r'":"\u0B43",
        "'s'": '',##
        "'t'": '',##
        "'u'":"\u0B42",
        "'v'":'\u0B4D\u0B27',
        "'w'":'\u0B4D\u0B71',
        "'x'":'\u0B03',  #/h
        "'y'":'\u0B2F\u0B4D\u0B5F', 
        "'z'":'\u0B4D\u0B37',         

        },
    "'S'": {            #Brace Control + char        
        "'A'":"\u0B3E",                     #A aa
        "'B'":'\u0B4D\u0B2C',       #B /ba
        "'C'":'\u0B4D\u0B1A',       #C /cha
        "'D'":'\u0B4D\u0B21',       #D /dda
        "'E'":"\u0B47",                     #E ae
        "'F'":'\u0B4D\u0B24',       #F /ta 
        "'G'":'\u0B4D\u0B17',       #G  /ga
        "'H'":'\u0B4D\u0B25',       #H  /tha                 
        "'I'":"\u0B3F",                       #I ii
        "'J'":'\u0B4D\u0B1C',         #J  /ja
        "'K'":'\u0B4D\u0B15',       #K  /ka
        "'L'":'\u0B4D\u0B32',       #L  /la
        "'M'":'\u0B4D\u0B2E',       #M /ma
        "'N'":'\u0B4D\u0B28',       #N /na
        "'O'":'\u0B4B',                     #O  oh
        "'P'":'\u0B4D\u0B2A',       #P /pa
        "'Q'":'',                                       #Q nothing
        "'R'":"\u0B4D\u0B30",       #R /ra
        "'S'":'\u0B4D\u0B38',                           #S  ??
        "'T'":'\u0B4D\u0B1F' ,      #T /ta
        "'U'":"\u0B41",                     #U  ou
        "'V'":'\u0B4D\u0B2D',       #V /bha
        "'W'":'\u0B4D\u0B71',       #W /va
        "'X'":'',                                       #X  /gyna
        "'Y'":'\u0B4D\u0B5F',       #Y /ya
        "'Z'":'\u0B4D\u0B36',        #Z /sha
          
        "'a'":"\u0B3E",                     #A aa
        "'b'":'\u0B4D\u0B2C',       #B /ba
        "'c'":'\u0B4D\u0B1A',       #C /cha
        "'d'":'\u0B4D\u0B21',       #D /dda
        "'e'":"\u0B47",                     #E ae
        "'f'":'\u0B4D\u0B24',       #F /ta 
        "'g'":'\u0B4D\u0B17',       #G  /ga
        "'h'":'\u0B4D\u0B25',       #H  /tha                 
        "'i'":"\u0B3F",                       #I ii
        "'j'":'\u0B4D\u0B1C',         #J  /ja
        "'k'":'\u0B4D\u0B15',       #K  /ka
        "'l'":'\u0B4D\u0B32',       #L  /la
        "'m'":'\u0B4D\u0B2E',       #M /ma
        "'n'":'\u0B4D\u0B28',       #N /na
        "'o'":'\u0B4B',                     #O  oh
        "'p'":'\u0B4D\u0B2A',       #P /pa
        "'q'":'',                                       #Q nothing
        "'r'":"\u0B4D\u0B30",       #R /ra
        "'s'":'\u0B4D\u0B38',                           #S  ??
        "'t'":'\u0B4D\u0B1F' ,      #T /ta
        "'u'":"\u0B41",                     #U  ou
        "'v'":'\u0B4D\u0B2D',       #V /bha
        "'w'":'\u0B4D\u0B71',       #W /va
        "'x'":'',                                       #X  /gyna
        "'y'":'\u0B4D\u0B5F',       #Y /ya
        "'z'":'\u0B4D\u0B36',        #Z /sha
            },
    "'T'":   {           #Loop throguh special odia characters one by one
        "'a'":"",
        "'b'":'',
        "'c'":'\u0B1E',
        "'d'":'\u0B3C',
        "'e'":"\u0B48",   
        "'f'":'',
        "'g'":'\u0B19',
        "'h'":'',
        "'i'":'',   
        "'j'":'\u0B1E',
        "'k'":'\u0B19',
        "'l'":'\u0B62',
        "'M'":'\u0B02',
        "'n'":'\u0B01',
        "'o'":'',   
        "'p'":'',
        "'q'":'\u0965',
        "'r'":'',
        "'s'":'',
        "'t'":'',
        "'u'":"\u0B44",
        "'v'":'',
        "'w'":'',
        "'x'":'\u0B3D',
        "'y'":'', 
        "'z'":'\u0B70',   
            }    
    }
  
  
  
valid_od_char = list(characterMap.keys() )
dependent_char_char = list(next_map.keys() )
Second_entry = list(next_map["'F'"].keys() )

def callback(event):
    text_box.focus_set()
    #print ("clicked at", event.x, event.y)
text_box = Text(root, width =30, height = 10 ,  font=("Helvetica", 32))
#text_box.insert("1.0", sample_text)
text_box.bind("<Key>", key)
text_box.bind("<Button-1>", callback)
text_box.config(state="disabled")
text_box.pack()
root.mainloop()

#=====
'''
text.delete(1.0, END)
text.insert(END, contents)
print (text_box.get("1.0",END))

'''




