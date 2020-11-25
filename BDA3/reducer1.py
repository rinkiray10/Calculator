#!/usr/bin/env python3
 
import sys
from pprint import pprint
 
weather_info = []
for lines in sys.stdin:
  
   line = lines.strip().split()
 
   weather_info.append(line)
 
 
minIndex, maxIndex,minimumTemp, maximumTemp = -1, -1, 10000, -10000
for i in range(len(weather_info)):
 
   if minimumTemp > float(weather_info[i][5]):
       minIndex = i
       minimumTemp = float(weather_info[i][5] )
 
   if maximumTemp < float(weather_info[i][9]):
       maxIndex = i
       maximumTemp = float( weather_info[i][9] )
 
 
print(f"{weather_info[minIndex][0]} {weather_info[minIndex][1]} Time: {weather_info[minIndex][3]} MinTemp : {weather_info[minIndex][5]}")
print(f"{weather_info[maxIndex][0]} {weather_info[maxIndex][1]} Time: {weather_info[maxIndex][7]} MaxTemp : {weather_info[maxIndex][9]}")   

