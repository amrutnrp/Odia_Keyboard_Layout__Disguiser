from tkinter import *

root = Tk()
print('Programm starting...')
chr_pressed =None
flag=0
import re


#=====================================================================================
def key(event):
    kp = repr(event.char)
    print ("pressed", kp,  len(kp), event.char) #repr(event.char))
    global chr_pressed
    chr_pressed = kp
        
        
    
    

def callback(event):
    text_box.focus_set()
    #print ("clicked at", event.x, event.y)
text_box = Text(root, width =70, height = 30)
#text_box.insert("1.0", sample_text)
text_box.bind("<Key>", key)
text_box.bind("<Button-1>", callback)
text_box.pack()
root.mainloop()

#=====
'''
text.delete(1.0, END)
text.insert(END, contents)
print (text_box.get("1.0",END))

'''



