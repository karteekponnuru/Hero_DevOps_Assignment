import psutil
import time

cpu_use = 0
stop_it = False

while stop_it == False:
    cpu_use = psutil.cpu_percent(interval=1)
    if cpu_use > 80:
        if cpu_use > 80:  
            print("Alert! CPU usage exceeds threshold:", cpu_use, "%")
    if cpu_use <= 80:
        print("CPU is fine now:", cpu_use, "%")
    if cpu_use == 0:
        cpu_use = psutil.cpu_percent(interval=1)  
