import os
import psutil
loadi,loads,load15 = psutil.getloadavg()
print(load15,loadi,loads)
cpu_usage = ((load15/os.cpu_count()) *100)
# Importing the library
print('The CPU usage is: ', psutil.cpu_percent(1))
print('RAM memory % used:', psutil.virtual_memory()[2])
print("the cpu usage is : ",cpu_usage)