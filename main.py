# Code By Nikolis32 #

# All Python Tools #
from queue import Queue
from plyer import notification
from colorama import *
from pystyle import *
from os import * 

import subprocess
import time
import socket
import threading
print_lock = threading.Lock()

# main code #
subprocess.check_call(["attrib","+H","README.md"])
system('title Welcome to ATEH Port Scanner by ɴɪᴋᴏʟɪꜱ32#9752.')
time.sleep(3)
system('title For help join in discord: https://discord.gg/MdkqRtzzWQ')

print(f"""{Fore.RED}
      
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
             ░ ░     ░                       ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                                ░                                                        
                                                            By ɴɪᴋᴏʟɪꜱ32#9752
                                                            GitHub https://github.com/ATEHgr
                                                            discord https://discord.gg/MdkqRtzzWQ
""") 

target = input(f"{Fore.MAGENTA}Enter target: ")
ip = socket.gethostbyname(target)

notification.notify(
            app_name = "[System] Port Scanning" ,
            title = "[System] Hello user I am Nikolis32 and I scan your ip:" ,
            message=    ip ,
            timeout=60 )


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('Port',port,": Open")
        con.close()
    except:
        pass



def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()



        


q = Queue()
for x in range(30):
     t = threading.Thread(target=threader)
     t.daemon = True
     t.start()


start = time.time()

# Ports 1-9999

for worker in range(1,9999):
    q.put(worker)

q.join()

# code by Nikolis32 #
