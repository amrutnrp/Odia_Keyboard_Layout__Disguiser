# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:00:27 2021

@author: amrut
"""

control_inp_types = {
"'\\x01'":'CTRL-A',
"'\\x02'":"CTRL-B", 
"'\\x03'":"CTRL-C", 
"'\\x04'":"CTRL-D", 
"'\\x05'":"CTRL-E", 
"'\\x06'":"CTRL-F", 
"'\\x07'":"CTRL-G", 
"'\\x08'":"CTRL-H",
"'\\t'"  :"CTRL-I",
"'\\n'"  :"CTRL-J",  
"'\\x0b'":"CTRL-K",  
"'\\x0c'":"CTRL-L",  
"'\\r'" :"CTRL-M",
"'\\x0e'":"CTRL-N", 
"'\\x0f'":"CTRL-O", 
"'\\x10'":"CTRL-P", 
"'\\x11'":"CTRL-Q", 
"'\\x12'":"CTRL-R", 
"'\\x13'":"CTRL-S",  
"'\\x14'":"CTRL-T", 
"'\\x15'":"CTRL-U",
"'\\x16'":"CTRL-V", 
"'\\x17'":"CTRL-W",
"'\\x18'":"CTRL-X", 
"'\\x19'":"CTRL-Y",
"'\\x1a'" :"CTRL-Z" 
    }


from pynput.keyboard import Key, Listener
is_shift = False
is_ctrl = False


def on_press(key):
    pass
    global is_shift, is_ctrl
    # print('{0} pressed'.format( key))
    # if key == Key.shift:
    #     is_shift = Truescalk
    if key == Key.ctrl_l or key == Key.ctrl_r:
        is_ctrl= True

def on_release(key):
    global is_shift, is_ctrl
    if key == Key.esc:
        # Stop listener
        return False
    elif key == Key.shift:
        is_shift = False
        return
    elif key == Key.ctrl_l or key == Key.ctrl_r:
        is_ctrl= False
        # a= '{0}'.format(key)
        # a= control_inp_types[a]
    elif key == Key.space:
        print (' ', end = '')
    elif key == Key.backspace:
        print ('<Bksp>', end = '')
    elif key==Key.enter:
        print ('\n', end = '')
    elif key == Key.tab:
        print ('\\t', end = '')
    else:
        a= '{0}'.format(key)
        
        if is_ctrl ==True:
            a= '<'+ control_inp_types[a] +  '>'
        if len(a) == 3:
            a= a[1]
        print('{}'.format(a), end = '')
        
        
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
