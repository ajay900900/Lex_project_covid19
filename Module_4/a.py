import os
import datetime
import subprocess
import os

clear_command = 'cls' if os.name == 'nt' else 'clear'
while True:
    resposne=""
    print("1. Scrape contry  Covid19 stats during covid ")
    print("2. Get news  between A time Range")
    print("3. Get Responses data between a Time Range")
    import subprocess

    print("4. Exit")
    
    response = input("Please select an option (1/2/3/4): ")
    import datetime

    if response == '1':
    	subprocess.run(["python3", "Module_3_1/3_1.py"])   
    reesponse=""
    if response == '2':
        path = 'Module_3.2_saurabh/module_3_2_news'  # Make sure to replace this with your target directory
        os.chdir(path)
        subprocess.run(["python3", "driver_32_saurav.py"])
    import subprocess

    if response == '3':
        path = 'Module_3.2_saurabh/module_3_2_res'  # Make sure to replace this with your target directory
        os.chdir(path)
        subprocess.run(["python3", "driver.py"])
    x=1
    if response == '4':
        exit()
    
