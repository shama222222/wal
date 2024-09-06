import os,requests,time
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool  

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
⠀⠀ ⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣄[Abhayki maa]⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
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


                                                         
{R}[{G1}+{R}]{G1}Decode{G1}━{R}>{G1}Marshal.Zlib.Decompress.Base64.B64decode
{R}[{G1}+{R}]{G1}Yourname{G1}━{R}>{G1}{name}
"""

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
        tks = 'L3G3ND%20S9UR4V%20BHAI%20MY%20NAME%20IS%20' +Nam + '%20PLEASE%20APPROVED%20MY%20KEY%20AND%20MY%20KEY%20IS%20:%20'+key1
        os.system('am start https://wa.me/+919106391471?text=' + tks)
        sys.exit()        
 
def main_dec():
	os.system('clear')
	print(logo)
	try:
		open("/data/data/com.termux/files/usr/bin/pycdc")
		open("/data/data/com.termux/files/usr/lib/python3.11/minopyc.py", "r").read()
		open("/data/data/com.termux/files/usr/bin/pycdas")
	except:
		os.system("curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdc")
		os.system("curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdas")
		os.system("curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/minopyc.py")
		os.system("mv pycdc /data/data/com.termux/files/usr/bin/")
		os.system("mv pycdas /data/data/com.termux/files/usr/bin/")
		os.system("mv minopyc.py /data/data/com.termux/files/usr/lib/python3.11/")
		os.system("chmod 777 /data/data/com.termux/files/usr/lib/python3.11/minopyc.py")
		os.system("chmod 777 /data/data/com.termux/files/usr/bin/pycdc")
		os.system("chmod 777 /data/data/com.termux/files/usr/bin/pycdas")
	try:
		file=input(f"{R}[{G1}+{R}]{G1} INPUT YOUR FILE : ")
		open(file)
		os.system(f"cp {file} .Rahul.py")
	except:
		exit('Nawaka Hallaya')
	try:
		open(file).read()
	except:
		os.system(f"pycdc .Rahul.py > .a.py")
		files = open(".a.py", "r").read()
		if "exec(str(chr" in files:
			c= files.split(']')[0]+"]\nprint(''.join([chr(i) for i in _]))"
			files = open(".a.py", "w").write(c)
			os.system("python3 .a.py > .Rahul.py")
		else:
			os.system("mv .a.py .Rahul.py")
			pass
	print(f'{R}[{G1}+{R}]{G1} PLEASE WAIT I WILL TRYING TO DECODING')
	while True:
		file = open(".Rahul.py", "r").read()
		if "(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(b" in file:
			filer = file.split("exec(")[1]
			open(".Rahul.py", "w").write("import minopyc,marshal\ncode =("+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
			os.system("python3 .Rahul.py;pycdc .a.py > .Rahul.py")
		elif "(__import__('marshal').loads(__import__('marshal').loads(__import__('marshal').loads(" in file:
			filer = file.split("exec(")[1]
			open(".Rahul.py", "w").write("import minopyc,marshal\ncode =("+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
			os.system("python3 .Rahul.py;pycdc .a.py > .Rahul.py")
		elif "exec(_(" in file:
			
			c= file.split('exec(_(')[1]
			l = ("import marshal,zlib,base64,minopyc\nx = (("+c+"\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') ")
			open(".Rahul.py","w").write(l)
			os.system("python .Rahul.py")
			os.system("pycdc .a.py > .Rahul.py")
		elif "exec((_)(" in file:
			c= file.split('exec((_)(')[1]
			l = ("import marshal,zlib,base64,minopyc\nx = (("+c+"\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') ")
			open(".Rahul.py","w").write(l)
			os.system("python .Rahul.py")
			os.system("pycdc .a.py > .Rahul.py")
		elif "exec(marshal.loads" in file:
			filer = file.replace("exec(", "code=(")
			open(".Rahul.py", "w").write("import minopyc,marshal\n"+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
			os.system("python3 .Rahul.py;pycdc .a.py > .Rahul.py")
		elif "exec((lambda __," in file:
			filer = file.replace("exec(", "print(")
			open(".a.py", "w").write(filer)
			os.system("python2 .a.py > .Rahul.py")
		else:
			c= open(".Rahul.py","r").read()
			if c == '':
				print(f'{R}[{G1}+{R}]{G1}THE TOOL CAN JUST DECODED DATA')
				save=input(f"{R}[{G1}+{R}]{G1}ENTER PATH TO SAVE FROM : ")
				os.system(f"pycdas .a.py > {save}")
				os.system("rm .a.py;rm .Rahul.py")
			elif "WARNING: Decompyle incomplete" in c:
				print(f'{R}[{G1}+{R}]{G1}THE TOOL CAN JUST DECODED DATA')
				save=input(f"{R}[{G1}+{R}]{G1}ENTER PATH TO SAVE FROM : ")
				os.system(f"pycdas .a.py > {save}")
			else:
				print(f'{R}[{G1}+{R}]{G1}THE TOOL DECODED')
				save=input(f"{R}[{G1}+{R}]{G1}ENTER PATH TO SAVE FROM : ")
				open(save, "w").write(c)
				break
			break
	try:
		open(".a.py")
		os.system("rm .a.py")
		try:
			open(".Rahul.py")
			os.system("rm .Rahul.py")
		except:pass
	except:pass
	exit(f"{R}[{G1}+{R}]{G1}DECODE DONE🤑🤑Kalyan mitro")
def contact_admin():
	os.system('xdg-open https://facebook.com/groups/1036123894351028/')

app = ('''

     _    ____  ____  ____   _____     ___    _     
    / \  |  _ \|  _ \|  _ \ / _ \ \   / / \  | |    
   / _ \ | |_) | |_) | |_) | | | \ \ / / _ \ | |    
  / ___ \|  __/|  __/|  _ <| |_| |\ V / ___ \| |___ 
 /_/   \_\_|   |_|   |_| \_\\___/  \_/_/   \_\_____|
                                                    
''')
main_dec()
