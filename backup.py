import shutil
import os
from datetime import date
import sys


def backup(src_file_name,dst_file_name,src_dir='',dst_dir=''):
    
    print(src_file_name,src_dir,dst_dir,dst_file_name)
    try:
        today = date.today()   
        date_format = today.strftime("%d_%b_%Y_") 
        src_dir = src_dir+src_file_name 
        
        if not src_file_name: 
            print("Please give atleast the Source File Name") 
            exit() 
        try:
            if src_file_name and dst_file_name and src_dir and dst_dir: 
                src_dir = src_dir+src_file_name 
                dst_dir = dst_dir+dst_file_name 
            elif dst_file_name is None or not dst_file_name: 
                dst_file_name = src_file_name 
                dst_dir = dst_dir+date_format+dst_file_name 
            elif dst_file_name.isspace(): 
                dst_file_name = src_file_name 
                dst_dir = dst_dir+date_format+dst_file_name 
            else: 
                dst_dir = dst_dir+date_format+dst_file_name 
                shutil.copy2(src_dir, dst_dir)
                print("Backup Successful!")
        except FileNotFoundError: 
                print("File does not exists!,\Please give the complete path") 
    except PermissionError:   
        dst_dir = dst_dir+date_format+dst_file_name  
        shutil.copytree(src_file_name, dst_dir) 



Src_fol = r'C:\Python\Python_Assignments\source'
Des_fol = r'C:\Python\Python_Assignments\destination'

files = os.listdir(Src_fol)
for i in files:
   # print(i)
   # print(Src_fol)
   # print(Des_fol)
    backup(i,'',Src_fol,Des_fol)    
                
    
   
    
      



    
    