import requests
import random
import time
from datetime import datetime
import sys
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from time import sleep
import os
import http.server
import socketserver
import threading
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

 
:::'###::::'##::::'##:'##::: ##:'####::'######::'##::::'##::::
::'## ##::: ##:::: ##: ###:: ##:. ##::'##... ##: ##:::: ##::::
:'##:. ##:: ##:::: ##: ####: ##:: ##:: ##:::..:: ##:::: ##::::
'##:::. ##: ##:::: ##: ## ## ##:: ##::. ######:: #########::::
 #########:. ##:: ##:: ##. ####:: ##:::..... ##: ##.... ##::::
 ##.... ##::. ## ##::: ##:. ###:: ##::'##::: ##: ##:::: ##::::
 ##:::: ##:::. ###:::: ##::. ##:'####:. ######:: ##:::: ##::::
..:::::..:::::...:::::..::::..::....:::......:::..:::::..:::::

                                             
                                             
                                                
                                                
                                                

                                                             
               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡆[My Friend]⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣬⣉⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⠀⠀[Me]⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣍⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⢿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡟⢀⣿⣿⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣶⣄⠀⠀⣸⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣄[Hater's]⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⡟⠀⠹⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠇⢿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⠁⠀⣀⣈⠻⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⠟⠀⢸⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣷⣜⢿⣿⣿⣧⠀⠀⠀⠀⢀⣀⣈⡙⠛⠛⠋⠁⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣧⣝⣛⣡⣶⣶⣾⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿⡇⠀⢹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢠⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⢀⣿⣿⣿⣤⣤⣄⣀⣀⣀⡀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠻⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀                                              


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
\033[1;97m║\033[1;93m* \033[1;97mN4M3    \033[1;91m: \033[1;96mAVNISH MENTEL \033[1;97m                       
\033[1;97m║\033[1;93m* \033[1;97mRULL3X  \033[1;91m: \033[1;96mNO RUL3X N0 G9NG \033[1;97m         
\033[1;97m║\033[1;93m* \033[1;97mBR9ND   \033[1;91m: \033[1;96mMR M3NT3L H3R3  \033[1;97m             
\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;96mhttps://www.facebook.com/R4HULD0NH3R3\033[1;97m.   
\033[1;97m║\033[1;93m* \033[1;97mWH9TS99P N0. \033[1;91m: \033[1;96m+91 9106****71\033[1;97m                           
\033[1;97m╚═════════════════════════════════════════════════════════════╝

'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
    # Prompt Password 
def pas():
    print('\u001b[37m' + '---------------------------------------------------')
    password = input("Password : ") 
    print('--------------------------------------------')
    mmm = requests.get('https://pastebin.com/raw/tBBC9TVj').text

    if mmm not in password:
        print('[-] <==> Incorrect Password!')
        sys.exit()
        
pas()

    
venom()
print('''\033[1;32m[#] _ KATTAR HINDU == > [ Jai Shree Ram ❤️💪]\n''')
if int:
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    print('''\033[1;35m-=[ THIS IS MULTI CONVO + LOADER TOOL CREATED BY MR. SOURAV ]=-''')
    print('''\033[1;33m-=[ Contact Us :: https://www.facebook.com/R9HULD0NH3R3/]=-\n''')
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    i = datetime.now()
    print(i.strftime("\033[1;32m[#] SYSTEM STARTED TIME ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;32m[#] _ IITX Y0UR D9D == > [ MR. RAHUL X3 AVNISH ]\n''')
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
        tks = 'L3G3ND%20RAHUL%20BHAI%20MY%20NAME%20IS%20' +Nam + '%20PLEASE%20APPROVED%20MY%20KEY%20AND%20MY%20KEY%20IS%20:%20'+key1
        os.system('am start https://wa.me/+919106391471?text=' + tks)
        sys.exit()        
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S3 %p")
                if response.ok:
                    print("\033[1;33m[+] ANSH + ABHAY KA BAAP RAHUL ROBIN ON FIRE {} of Convo\033[1;35m {} \033[1;33msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;32m  - Time: {}".format(current_time))
                else:
                    print("\033[1;32m[x] FRESH TOKEN DALO ABHAY+ ANSH KI DD CHODNE KE LIYE  {} of Convo \033[1;34m{} with Token \033[1;36m{}: \n\033[1;36m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)
            print("\n\033[1;33m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;35m[!] An error occurred: {}".format(e))
def main():
 print(logo)
print(' \033[1;35m[+] 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘 ')
token_file = input(BOLD + CYAN + "=>").strip()
tokens = get_access_tokens(token_file)
print(' \033[1;34m[+] 𝗖𝗢𝗡𝗩𝗢 𝗜𝗗 ')
convo_id = input(BOLD + CYAN + "=>").strip()
print(' \033[1;33m[+] 𝗠𝗘𝗦𝗦𝗘𝗚𝗘 𝗙𝗜𝗟𝗘 ')
messages_file = input(BOLD + CYAN + "=> ").strip()
print(' \033[1;32m[+] 𝗛𝗔𝗧𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘 ')
haters_name = input(BOLD + CYAN + "=> ").strip()
print(' \033[1;36m[+] 𝗦𝗣𝗘𝗘𝗗 𝗦𝗘𝗖𝗢𝗡𝗗' )
speed = int(input(BOLD + CYAN + "======> ").strip())
with open(messages_file, 'r') as file:
        messages = file.readlines()
server_thread = threading.Thread(target=execute_server)
server_thread.start()
send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()
