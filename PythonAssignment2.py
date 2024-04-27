import psutil
import time 
import tkinter
from tkinter import messagebox

try:
    print("Monitoring CPU usage...")
    while True:
        print(f"{psutil.cpu_percent()} %")
        if(psutil.cpu_percent()>80.0):
            messagebox.showinfo(f"Alert! CPU usage exceeds threshold:{psutil.cpu_percent()}")
        elif(psutil.cpu_percent()>90.0):
            messagebox.showinfo("Alert! CPU usage exceeds threshold:",psutil.cpu_percent())
        time.sleep(1)
    
except KeyboardInterrupt:
    print("\nInterrupted!")
finally:
    print("Exiting the program.")
          
 
        
