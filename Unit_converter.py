# Copyright 2021 Yuhan yuhann@bu.edu
#!/usr/bin/env python

#User wants to convert a value from one unit to another unit
   #Units covered include:  
     #Meters to /from feet and inches or miles
     #(Kilo)Grams to/from ounces/pounds
     # Temperature C to/from F
import numpy as np

# meters to feet,inches,and miles
def meters(m):
  n_feet = n/0.3048
  n_inches = n*39.37
  n_miles = n/1609
  return round(n_feet,n_inches,n_miles,2)

# feet to meters
def feet(ft):
  n_meters = ft*0.3048
  return round(n_meters,2)

# Fahrenheit = (Celsius * 9/5) + 32
def CtoF(c):
  f = (c * 9 / 5) + 32
  return round(f, 2) 

# Celsius = (Fahrenheit – 32) * 5/9
def FtoC(f):
  c = (f - 32) * 5 / 9
  return round(c, 2) 
