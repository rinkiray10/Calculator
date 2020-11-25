#!/usr/bin/env python3
 
import sys
temperatures = {}
 
for lines in sys.stdin:
   line = lines.strip().split()
 
   city, date = line[0].split('_')
 
   for i in range(1,len(line),2):
       temperatures[line[i]] = float( line[i+1] )
 
   minTemperature= min(temperatures , key=temperatures.get)
   maxTemperature= max(temperatures , key=temperatures.get)
 
   min_max_temperature_time = f"{city} {date} Time: {minTemperature} MinTemp: {temperatures[minTemperature]} Time: {maxTemperature} MaxTemp: {temperatures[maxTemperature]}"
   print(min_max_temperature_time)

