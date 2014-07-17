#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

In Python how approximate a float to the nearest integer above?

En Python, ¿Cómo aproximar un float al entero más cercano por arriba?
'''

import math

#create a float number
f = 47.293
print(f)

#return ceiling of f, rounded to the nearest integer toward positive infinity
f_aprox = math.ceil(f)
print(f_aprox)

#create a float number
f = 42.837
print(f)

#approaches always made up
f_aprox = math.ceil(f)
print(f_aprox)
