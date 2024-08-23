import requests
import mechanize
import getpass
import json
import random
import time
from datetime import datetime
from bs4 import BeautifulSoup 
from colorama import Fore, Style
from rich.panel import Panel
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from os import system as sh
from time import sleep
 
os.system("xdg-open https://www.facebook.com/arti.raturi.184/?ref=share")
time.sleep(1)
 
def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')
            
def liness():
		print('\u001b[37m' + '[>] ================================')
		
		
cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;31;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;36;1m"
WHITE = "\033[1;30;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;36;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;32;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"


imt="-M4786=="
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'w')
	kok.write(myid+imt)
	kok.close()
def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """
 
 
 /$$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$ /$$      
| $$__  $$ /$$__  $$| $$  | $$| $$  | $$| $$      
| $$  \ $$| $$  \ $$| $$  | $$| $$  | $$| $$      
| $$$$$$$/| $$$$$$$$| $$$$$$$$| $$  | $$| $$      
| $$__  $$| $$__  $$| $$__  $$| $$  | $$| $$      
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$      
| $$  | $$| $$  | $$| $$  | $$|  $$$$$$/| $$$$$$$$
|__/  |__/|__/  |__/|__/  |__/ \______/ |________/
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()
print('''\033[1;33m---------------------------------------------------------------------\n''')
def venom():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    y = '''
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mN4M3    \033[1;91m: \033[1;96mSOURAV TIWARI \033[1;97m                       
\033[1;97m║\033[1;93m* \033[1;97mRULL3X  \033[1;91m: \033[1;96mNO RUL3X N0 G9NG \033[1;97m         
\033[1;97m║\033[1;93m* \033[1;97mBR9ND   \033[1;91m: \033[1;96mMR R9HUL H3R3  \033[1;97m             
\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;96mhttps://www.facebook.com/R4HULD0NH3R3\033[1;97m.   
\033[1;97m║\033[1;93m* \033[1;97mWH9TS99P N0. \033[1;91m: \033[1;96m+91 9106****71\033[1;97m                           
\033[1;97m╚═════════════════════════════════════════════════════════════╝

'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
venom()
print('''\033[1;32m[#] _ KATTAR HINDU == > [ Jai Shree Ram ❤️💪]\n''')
if int:
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    print('''\033[1;35m-=[ THIS IS MULTI Wall + POST LOADER TOOL CREATED BY MR. SOURAV ]=-''')
    print('''\033[1;33m-=[ Contact Us :: https://www.facebook.com/R9HULD0NH3R3/]=-\n''')
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    i = datetime.now()
    print(i.strftime("\033[1;32m[#] SYSTEM STARTED TIME ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;32m[#] _ IITX Y0UR D9D == > [ MR. RAHUL ]\n''')
    print("\033[1;36;40m", end = "")
    Nam = input(" WHAT IS YOUR NAME BRO: ")
    
    #---------------APPROVAL--------SYSTEM---------------#
    key1=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
    r1=requests.get("https://github.com/prema577/Approval/blob/main/approval.txt").text
    if key1 in r1:
        os.system('espeak -a 300 " YOUR, KEY,  IS,  SUCCESSFULLY,   APPROVED..."')
        liness()
        print(BOLD + CYAN + "YOUR KEY WAS SUCCESSFULLY APPROVED")
    else:
        os.system('espeak -a 300 " YOUR, KEY, NOT,   APPROVED..."')
        print(BOLD + RED + " YOUR KEY IS NOT APPROVED BRO ")
        sleep(3.5)
        liness()
        liness()
        input(BOLD + GREEN + " Press Enter To Send Key")
        time.sleep(3.5)
        tks = 'DEAR%20MAFIYA%20SIR%20MY%20NAME%20IS%20' +Nam + '%20PLEASE%20APPROVED%20MY%20KEY%20AND%20MY%20KEY%20IS%20:%20'+key1
        os.system('am start https://wa.me/+919106391471?text=' + tks)
        sys.exit()        
 
 
# Prompt for token file
token_file = input("ENTER TOKEN FILE PATH : ")
print('--------------------------------------------')
 
# Read access token IDs from file
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()
 
# Prompt for the number of user IDs
num_user_ids = int(input("HOW MANY POSTS YOU WANT FOR LOADER : "))
print('--------------------------------------------')
 
# Define the user IDs and message files
user_messages = {}
haters_name = {} 
 
# Prompt for user IDs and message files
for i in range(num_user_ids):
    user_id = input(f"ENTER POST ID #{i+1} : ")
    print('--------------------------------------------')
    hater_name = input(f"ENTER HATER NAME FOR POST ID {user_id} : ")
    print('--------------------------------------------')
    haters_name[user_id] = hater_name
    message_file = input(f"ENTER MESSAGES FILE /NP FOR {user_id} : ")
    print('--------------------------------------------')
    user_messages[user_id] = message_file
 
 
 
 
# Prompt for delay time in messages
delay_time = int(input("ENTER DELAY/TIME (in seconds) FOR MESSAGES : "))
print('--------------------------------------------')
 
# Prompt for delay before repeating the process
repeat_delay = int(input("ENTER DELAY/TIME (in seconds) BEFORE REPEATING THE PROCESS : "))
print('--------------------------------------------')
 
# Get profile name using an access token
def get_profile_name(access_token):
    url = f'https://graph.facebook.com/v17.0/me?access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    if 'name' in data:
        return data['name']
    return None
 
# Function to send a message to a user's inbox conversation using an access token
def send_message(access_token, user_id, message):
    url = "https://graph.facebook.com/v15.0/{}/comments".format(user_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Referer': 'https://www.facebook.com/',
        'Authorization': f'Bearer {access_token}'
    }
    data = {'message': hater_name + ' ' + message}
 
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{Fore.BLUE}[{current_time}] {Fore.YELLOW}Comment sent successfully to user ID {user_id}: {Fore.GREEN}{hater_name + message}')
        return True
    else:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{Fore.BLUE}[{current_time}] {Fore.RED}Error sending comment to user ID {user_id}: {Fore.RED}{hater_name + message}')
        print(f'{Fore.RED}[{current_time}] Response content: {Fore.RED}{response.content.decode()}')
        return False
 
# Main loop to send messages
while True:
    total_successful_messages = 0
    total_unsuccessful_messages = 0
 
    # Iterate over the access tokens
    for i, access_token in enumerate(access_tokens):
        try:
            # Login using the access token and get the profile name
            profile_name = get_profile_name(access_token)
            if not profile_name:
                continue
 
            profile_number = i + 1
            access_token_id = access_token[:4] + '********'
 
            # Print the profile information
            print('--------------------------------------------')
 
            # Iterate over the user IDs and messages
            for user_id, message_file in user_messages.items():
            	
                # Read messages from the message file for the current user ID
                with open(message_file, 'r') as f:
                    messages = f.read().splitlines()
 
                # Shuffle the messages for the current user
                
                # Get the hater name for the current user ID
                hater_name = haters_name[user_id]
 
 
                # Get the messages count for the current user
                messages_count = len(messages)
 
                # Get the current message index for the user ID
                message_index = i % messages_count
 
                # Get the message for the current index
                message = messages[message_index]
 
                if send_message(access_token, user_id, message):
                    total_successful_messages += 1
                else:
                    total_unsuccessful_messages+= 1
 
                time.sleep(delay_time)  # Delay between each message
            # Print Facebook ID, message, and current date/time after message is sent
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{Fore.MAGENTA}Facebook ID: {user_id}')
            print('--------------------------------------------')
            print('Next ID Ready To Send Comment')
            print('--------------------------------------------')
 
        except requests.exceptions.RequestException as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{Fore.RED}[{current_time}] Internet disconnected. Reconnecting in 10 seconds...{Style.RESET_ALL}')
            time.sleep(10)
 
        except Exception as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            continue
 
    print('--------------------------------------------')
    print('All comments sent. Waiting before repeating the process...')
    print('--------------------------------------------')
    time.sleep(delay_time)  # Delay before repeating the process
 
