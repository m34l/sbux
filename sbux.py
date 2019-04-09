import requests
import sys
import os
import termcolor
import json
import time
from datetime import datetime

class warna:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
ismail	= warna.HEADER + "  __       __   ______   __    __  __ \n" + warna.ENDC      
gtg     = warna.HEADER + " /  \     /  | /      \ /  |  /  |/  |\n" + warna.ENDC      
banget  = warna.HEADER + " $$  \   /$$ |/$$$$$$  |$$ |  $$ |$$ |\n" + warna.ENDC      
tampan  = warna.HEADER + " $$$  \ /$$$ |$$ ___$$ |$$ |__$$ |$$ |\n" + warna.ENDC      
sekalih = warna.HEADER + " $$$$  /$$$$ |  /   $$< $$    $$ |$$ |\n" + warna.ENDC      
m34l    = warna.HEADER + " $$ $$ $$/$$ | _$$$$$  |$$$$$$$$ |$$ |\n" + warna.ENDC      
ganteng = warna.HEADER + " $$ |$$$/ $$ |/  \__$$ |      $$ |$$ |_____\n" + warna.ENDC 
bgt     = warna.HEADER + " $$ | $/  $$ |$$    $$/       $$ |$$       |\n" + warna.ENDC
mantap  = warna.HEADER + " $$/      $$/  $$$$$$/        $$/ $$$$$$$$/\n" + warna.ENDC 
exit = "[========]"
for l in w:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
for l in gans:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
for l in sangat:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
for l in coded:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
for l in me:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.01)
print warna.BOLD + warna.WARNING + "                       M34L\n" + warna.ENDC + warna.ENDC
kontol = str(raw_input("Enter Mailist File: "))
openfile = open(kontol, 'r')
url = 'https://m34lnetwork.co.id/sbux/check.php'
start_time = time.time()
for i in openfile:
    try:
        r = requests.post(url, data={'data':str(i).replace(' ', '')}, verify=False)
    except requests.exceptions.ConnectionError:
        print "[TIMEOUT]", i
    if "LIVE" in r.text:
        print warna.OKGREEN + str(r.text).replace('\n', '') + warna.ENDC
        live = r.text
        tanggal = datetime.today()
        dtwithoutseconds = tanggal.replace(second=0, microsecond=0)
        date = str(dtwithoutseconds).replace(':', '_').replace(' ', '_')
        filename = u"LIVE-%s.txt"%date
        save = open(filename, 'a')
        save.write(str(live)+'\n')
        save.close()
    elif "DIE" in r.text:
        print warna.FAIL + r.text + warna.ENDC
    elif "UNCHECKED" in r.text:
        print warna.WARNING + "UNCHECKED" + i + warna.ENDC
    else:
        print "Unknown Error, please contact admin"
elapsed_time = time.time() - start_time
print "[+] Job Done!"
print "[+] Total Time: ",elapsed_time
print "[+] Result was Saved as LIVE-{}.txt".format(date)
