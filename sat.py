#!/home/erwann/Documents/side-code/sat/venv/bin/python3
import requests
import subprocess
import os
from datetime import datetime
#r = requests.get("https://imn-api.meteoplaza.com/v4/nowcast/tiles/satellite-europe-visible/202402101700/5/8/14/14/20")
#On a 1h30 de decalage
#https://www.sat24.com/fr-fr#selectedLayer=euMicro


now = datetime.now()

year = str(now.year)

day =  str(now.day)
if len(day) == 1:
    day = '0' + day

month = str(now.month)
if len(month) == 1:
    month = '0' + month

hour = str(now.hour - 2)
if len(hour) == 1:
    hour = '0' + hour

minute = str((now.minute//15)*15)
if len(minute) == 1:
    minute = '0' + minute


time = year + month + day + hour + minute
print(time)
print(year, month, day, hour, minute)
#/v4/nowcast/tiles/satellite-europe-visible/202402111730/5/6/12/14/21

#url = "https://imn-api.meteoplaza.com/v4/nowcast/tiles/satellite-europe-visible/"+time+"/5/6/12/14/21"
url = "https://imn-api.meteoplaza.com/v4/nowcast/tiles/satellite-europe/"+time+"/5/9/13/14/20"
print(url)
commande_bash = "swww img --transition-fps 60 /home/erwann/Pictures/earth.png"

response = requests.get(url)
if response.status_code == 200:
    with open("/home/erwann/Pictures/earth.png", 'wb') as f:
        f.write(response.content)
        #subprocess.run("swww img /home/erwann/Pictures/earth.png")
        os.system("swww img /home/erwann/Pictures/earth.png")

else:
    print(response.status_code)
