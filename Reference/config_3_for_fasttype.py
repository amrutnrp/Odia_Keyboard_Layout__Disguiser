# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 10:52:15 2021

@author: amrut
"""

from Import_odia_process_3 import *



def formalize (a,b, c = ''):
    if a== '' or b== '':
##        print (a+b +'got excempted')
        return
    print ('[ \'{}{}\', \'{}\' ],'.format( a, c, b))

############excempt_list = []
############for i in Number_map:
############      if i in excempt_list :
############          continue
############      formalize( i, Number_map[i] )
##############
##########char -> h
##excempt_list = []
##for i in range (26):
##    if i in excempt_list :
##        continue    
##    formalize(result_LUT[i],result_LUT[26+i], 'h')
##
############char -> f
##excempt_list = []
##for i in range (26):
##    if i in excempt_list :
##        continue    
##    formalize(result_LUT[i],result_LUT[26+26+i], 'f')
############## normal char 
##excempt_list = []
##for i in range (26):
##    if i in excempt_list :
##        continue    
##    formalize(chr(97+i),result_LUT[i])

##########now capitala
##excempt_list = []
##for i in range (26):
##    if i in excempt_list :
##        continue    
##    formalize(chr(65+i),result_LUT[i+26*3])
##
##
##
###########  F-> H
##excempt_list = []
##for i in range (26):
##    if i in excempt_list :
##        continue    
##    formalize( result_LUT[i+26*2],result_LUT[i+26*4], 'h')

###########  H -> F
##excempt_list = []
##for i in range (26):
##    if i in excempt_list :
##        continue    
##    formalize( result_LUT[i+26],result_LUT[i+26*4], 'f')
##
###########  Capital H
##excempt_list = []
##for i in range (26):
##    if i in excempt_list :
##        continue    
##    formalize( result_LUT[i+26*3],result_LUT[i+26*5], 'h')
##
############# ` + char
##
excempt_list = []
for i in range (26):
    if i in excempt_list :
        continue    
    formalize( result_LUT[i],result_LUT[i+26*6], '//')
##
##
##
##for i in range (26):
##    formalize( ' ',result_LUT[i+26*7], chr(97+i))

##      
##for i in range (26):
##    formalize( '\\u200c?',result_LUT[i+26*7], chr(97+i))





    
