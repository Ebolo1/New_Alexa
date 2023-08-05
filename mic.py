# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:26:30 2023

@author: Ing.Ebolo Hsmiley
"""
import speech_recognition as s_r

present = s_r.Microphone.list_microphone_names()
print(present[1])

