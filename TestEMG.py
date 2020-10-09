# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:18:04 2020

@author: lkvan
"""

# Use one of the filters on a user button input and send result to uScope
import br_timer 
import br_serial
from machine import Pin, ADC

pc = br_serial.serial_pc(1)
def loop():
    adc = ADC(Pin('A0'))
    # Read value of 16bit ADC between 0-65535 corresponding to 0V-3.3V
    pc.set(0, adc.read_u16())
    pc.send()
    
t1 = br_timer.ticker(1, 300, loop)
t1.start()