#! /usr/bin/python3
import os
from time import sleep as timeout
import threading
import string
import base64
import urllib.request
import urllib.parse
import time
import sys
import random
from time import sleep
import platform
def clear ( ):
	if platform.system( ) == 'Windows':
		os.system("cls")
	elif platform.system( ) == 'Linux':
		os.system("clear")
	else:
		os.system ("clear")
#===================================#
W='\033[1;32m'
A='\033[1;33m'
B='\033[1;30m'
V= '\033[;36m'
D='\033[;0m'
VM='\033[1;31m'
M='\033[1;30m'
P='\033[1;31m'
G='\033[1;34m'
C='\033[36m'
H='\033[1;35m'


# interface de usuário é banner #
#======================================#
os.system("clear")
print("""
█████████
█▄█████▄█
█▼▼▼▼▼
█ Bem-vindo ao Shields Black!
█▲▲▲▲▲
█████████
 ██ ██
	""")
usuario = input("Digite nome de usuário ~>")
os.system("clear")


#======================================#


def menu():
	arquivo = open ("Imgs/Menu")
	print (arquivo.read ())
menu ()
	
def sair_do_programar():
	print(f"""
	
 {C}   __________
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
  ╔════════════╗
  ╚════════════╝{V}
 {B} ║██████████╚╗
  ║██{P}╔══╗{B}█{P}╔═╗{B}█║
  ║██{P}║╬╔╝{B}█{P}╚╗║{B}█║
  ║██{P}╚═╝{B}█║█{P}╚╝{B}█║
  ╚╗█████████═╝
     ╚╗║╠╩╩╩╩╩
        ║║┈┈┈█{C}▐█████{P}▒.｡oO
       {B} ║██╠╦╦╦╗
        ╚╗██████
           ╚════╝{B}
[VOLTE SEMPRE BROW]
""")

#construção da ferramenta#

while True:
    print(" ")
    opcao = input (f"""{C}
┌──({usuario}{P}㉿{G}Termux)-[{P}Shields-Black{C}]
└─$ """)
    
    if opcao == "a":
            def Packs():
            	banner = open("Imgs/packs")
            	print(banner.read ())
            	#selec = input("Digite sua opçao ->")
            	selec = input (f"""{C}
┌──({usuario}{P}㉿{G}Termux)-[{P}Shields-Black{C}]
└─$ """)
            	
            	
            	
            	if selec == "1":
            	    def findomain():
            	        os.system("apt-get update -y")
            	        os.system("apt-get upgrade -y")
            	        os.system("pkg install rust make perl -y")
            	        os.system("apt-get install findomain -y")
            	        print(f"{H}user:\nfindomain -help consultar menu.")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    findomain()
            	
            	elif selec == "2":
            	    
            	    def config():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/403ForbiddenF1/configurar_termux")
            	        os.system("mv configurar_termux /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    config()
            	
            	elif selec == "3":
            	    def koroni():
            	        os.system ("termux-setup-storage")
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system ("pkg install git -y")
            	        os.system("pkg install php -y")
            	        os.system("git clone https://github.com/DeepSociety/koroni")
            	        os.system("mv koroni /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    koroni()
            	
            	elif selec == "4":
            	    def zphisher():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -h")
            	        os.system("pkg install php -y")
            	        os.system("git clone  git://github.com/htr-tech/zphisher.git")
            	        os.system("mv zphisher /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    zphisher()
            	
            	elif selec == "5":
            	    def fotosploit():
            	        os.system ("apt update -y")
            	        os.system ("pkg upgrade -y")
            	        os.system ("pkg install git -y")
            	        os.system("pkg install php -y")
            	        os.system("git clone https://github.com/Cesar-Hack-Gray/FotoSploit")
            	        os.system("mv FotoSploit /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    fotosploit()
            	
            	elif selec == "6":
            	    def weeman():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("pkg install python -y")
            	        os.system("git clone https://github.com/evait-security/weeman")
            	        os.system("mv weeman /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    weeman()
            	
            	elif selec == "7":
            	    def sqlmap():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/sqlmapproject/sqlmap")
            	        os.system("mv sqlmap /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    sqlmap()
            	
            	elif selec == "8":
            	    def impulse():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system ("pkg install python2 -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/LimerBoy/Impulse")
            	        os.system("mv Impulse /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    impulse()
            	
            	elif selec == "9":
            	    def URLSpoof():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/Darkmux/URLSpoof")
            	        os.system("mv URLSpoof /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    URLSpoof()
            	
            	elif selec == "10":
            	    def lazymux():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install python2 -y")
            	        os.system("git clone https://github.com/Gameye98/Lazymux")
            	        os.system("mv Lazymux /data/data/com.termux/files/home")
            	        os.system("mv lazymux.conf /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    lazymux()
            	
            	elif selec == "11":
            	    def wifite():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install python2 -y")
            	        os.system("pkg install git -y")
            	        os.system(" git clone https://github.com/derv82/wifite")
            	        os.system("mv wifite /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    wifite()
            	
            	elif selec == "12":
            	    def fbi():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install python2 -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/xHak9x/fbi.git")
            	        os.system("mv fbi /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    fbi()
            	elif selec == "13":
            	    def papaviruz():
            	        os.system("pkg update -y") 
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install bash -y")
            	        os.system("pkg install pv -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/Hacking-pch/papaviruz")
            	        os.system("mv papaviruz/ /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    papaviruz()
            	elif selec == "14":
            	    def kiny():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install python2 -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/Kiny-Kiny/Kiny-Painel")
            	        os.system("mv Kiny-Painel /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    kiny()
            	
            	elif selec == "15":
            	    def spamwa():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install python2- y")
            	        os.system("git clone https://github.com/sandiwijayani1/SpamWa")
            	        os.system("mv SpamWa /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    spamwa()
            	
            	elif selec == "16":
            	    def wifihacker():
            	        os.system ("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system ("pkg install git -y")
            	        os.system("git clone https://github.com/esc0rtd3w/wifi-hacker")
            	        os.system("mv wifi-hacker /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    wifihacker()
            	
            	elif selec =="17":
            	    def fish():
            	        os.system ("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install python2 -y")
            	        os.system("git clone https://github.com/UndeadSec/SocialFish")
            	        os.system("mv SocialFish /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    fish()
            	
            	
            	elif selec == "18":
            	    def routersploit():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("termux-setup-storage")
            	        os.system ("pkg install python git clang -y")
            	        os.system("pkg install -y")
            	        os.system("pkg install make -y")
            	        os.system ("pkg install python -y")
            	        os.system ("git clone https://github.com/threat9/routersploit")
            	        os.system("mv routersploit /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    routersploit()
            	
            	elif selec == "19":
            	    def nexphisher():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/htr-tech/nexphisher")
            	        os.system("mv nexphisher /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    nexphisher()
            	
            	elif selec == "20":
            	    def ngrok():
            	        os.system("apt upgrade -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/PSecurity/ps.ngrok")
            	        os.system("mv ps.ngrok /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    ngrok()
            	
            	elif selec == "21":
            	    def kalischemes4termux():
            	        os.system("apt update -y")
            	        os.system("apt upgrade -y")
            	        os.system("apt install git -y")
            	        os.system("git clone https://gitlab.com/sidneypepo/kalischemes4termux")
            	        os.system("mv kalischemes4termux /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    kalischemes4termux()
            	
            	elif selec == "22":
            	    def tstyling():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/darkwarrior3/tstyling")
            	        os.system("mv tstyling /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    tstyling()
            	
            	elif selec == "23":
            	    def metasploit():
            	        os.system("apt update -y")
            	        os.system ("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/rapid7/metasploit-framework")
            	        os.system("mv metasploit-framework /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    metasploit()
            	
            	elif selec == "24":
            	    def lazyfiglet():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/TechnicalMujeeb/LazyFiglet.git")
            	        os.system("mv LazyFiglet /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    lazyfiglet()
            	
            	elif selec == "25":
            	    def red_hawk():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("pkg install php -y")
            	        os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
            	        os.system("mv RED_HAWK /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    red_hawk()
            	
            	elif selec == "26":
            	    def spamrito():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/MisterIot/spamrito")
            	        os.system("mv spamrito /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    spamrito()
            	
            	elif selec == "27":
            	    def Tool():
            	        os.system("apt update -y")
            	        os.system("pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/rajkumardusad/Tool-X")
            	        os.system("mv Tool-X /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    Tool()
            	
            	elif selec == "28":
            	    def wpscan():
            	        os.system("apt update -y")
            	        os.system ("apt upgrade -y")
            	        os.system("apt install git -y")
            	        os.system("apt install ruby -y")
            	        os.system("git clone https://github.com/wpscanteam/wpscan.git")
            	        os.system("mv wpscan /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    wpscan()
            	
            	elif selec == "29":
            	    def torshammer():
            	        os.system("apt update -y && pkg upgrade -y")
            	        os.system("pkg install python -y")
            	        os.system("pkg install python2 -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/dotfighter/torshammer")
            	        os.system("mv torshammer /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    torshammer()
            	
            	elif selec == "30":
            	    def clis():
            	        os.system("apt update -y && pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/Olliv3r/clis")
            	        os.system("mv clis /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    clis()
            	
            	elif selec == "31":
            	    def aiophish():
            	        os.system("apt update -y && pkg upgrade -y")
            	        os.system("pkg install git -y")
            	        os.system("git clone https://github.com/DeepSociety/AIOPhish")
            	        os.system("mv AIOPhish /data/data/com.termux/files/home")
            	        print(f"{P}Instalação concluída...");timeout(3);
            	        print("~"*27)
            	        print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
            	    aiophish()
            	
#TERMINADOR DAQUI PRA BAIXO#
#===========================#
            	elif selec == "99":
            	    def menu_principal():
            	        print(f"{G}Voltando ao menu Inicial...");timeout(1);
            	        os.system("clear")
            	        menu()
            	    menu_principal()
            	    
            	elif selec == "00":
            	    def sair():
            	        os.system("clear")
            	        sair_do_programar()
            	        print("SAINDO DO PROGRAMAR....");timeout(3);
            	        exit()
            	    sair()
            	
            	
            	else:
            	    print("~"*25)
            	    print(f"{P}Opção Inválida, escolhar somenter as Opção do menu.:(");timeout(3);
            	    print(f"{C}~"*25)
            	    os.system ("clear")
            	    Packs()
            	
            Packs()
            
    elif opcao == "b":
        def sheldres_sms():
            az='\033[36m'
            V='\033[1;32m'
            D='\033[;0m'
            VM='\033[1;31m'
            B='\033[1;34m'
            C='\033[1;37m'
            CY='\033[1;36m'
            A='\033[1;33m'
            R='\033[1;35m'
            MG='\033[1;95m'
            M='\033[1;35m'
            def banner( ):
            		print (f'''

{az}
    ███████╗██╗  ██╗███████╗██╗     ██████╗ ██████╗ ███████╗███████╗
    ██╔════╝██║  ██║██╔════╝██║     ██╔══██╗██╔══██╗██╔════╝██╔════╝
    ███████╗███████║█████╗  ██║     ██║  ██║██████╔╝█████╗  ███████╗
    ╚════██║██╔══██║██╔══╝  ██║     ██║  ██║██╔══██╗██╔══╝  ╚════██║
    ███████║██║  ██║███████╗███████╗██████╔╝██║  ██║███████╗███████║
    ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                         {G}            :'######::'##::::'##::'######::
                                     '##... ##: ###::'###:'##... ##:
                                      ##:::..:: ####'####: ##:::..::
                       {H}              . ######:: ## ### ##:. ######::
                                     :..... ##: ##. #: ##::..... ##:
                             {P}        '##::: ##: ##:.:: ##:'##::: ##:
                                     . ######:: ##:::: ##:. ######::
                                     :......:::..:::::..:::......:::
=============================================================================
''')  
            try:
                import requests
            except ImportError:
                
                banner()
                input('Presione qualquer tecla para continuar')
                
            
            
            try:
                urllib.request.urlopen('https://www.google.com')
            except Exception:
                print (f"""{P}ERROR DE CONEXÃO!!! \nVOCÊ ESTÁ OFF-LINE NO MOMENTO! \nCONECTAR COM SUA INTERNET PARA CONTINUAR.""")
                input ("PRESSIONE ENTER PARA SAIR")
                print (f"{G}="*45)
                sleep (3)
                exit ()
            
            
            type = 1
            try:
            	if sys.argv[1] == "track":
            		type = 1
            except Exception:
            	type = 0
            if type == 4:
            	print("Ferramenta De mensagem anonimas")
            	print()
            elif type == 0:
            	while True:
            		clear ( )
            		banner ()
            		print(f" {V}Coloque os detalhes do número.\n Código do país [sem o +]")
            		cdp =input (f"""{az}
┌──({usuario}{P}㉿{G}Termux)-[{P}Shields-Black/SHELDRES-SMS{az}]
└─$ """)
            		if '+' in cdp:
            		        tc = list(cdp)
            		        tc.remove('+')
            		        cdp = ''.join(tc)
            		        cdp = cc.strip()
            		if len(cdp) >= 4 or len(cdp) < 1:
            		        print(f'\n{P}Codigo invalido..{A}\nGeralmente eles possuem 1 a 3 digitos..{D}.\n')
            		        sleep (2)
            		        continue
            		print(f"{az}Digite [DDD + NÚMERO]")
            		pn = input (f"""{az}
┌──({usuario}{P}㉿{G}Termux)-[{P}Shieazs-Black/SHELDRES-SMS{az}]
└─$ +{cdp} """)
            		if len(pn) <= 6:
            		        print(f'\n{P} Numero invalido\n')
            		        sleep(2)
            		        clear ( )
            		        continue
            		numbe = cdp + pn
            		if not numbe.isdigit():
            		            print('\n\nNumero de telefone tem que ter somente numeros\n')
            		            sleep(3)
            		            clear ( )
            		            continue
            		receiver = '+' + numbe
            		print(f"{az} Digite sua mensagem para ~~> +{cdp} {pn}")
            		text = input (f"""{az}
┌──({usuario}{P}㉿{G}Termux)-[{P}Shields-Black/SHELDRES-SMS{az}]
└─$ """)
            		try:
            		    
                		resp = requests.post('https://textbelt.com/text',{
                			'phone' : receiver,
                			'message' : text ,
                			'key' : 'textbelt'
            		})
            		except UnboundLocalError as erro:
            		    print ("="*36)
            		    print (f"{P}DEU ERRO EM ALGO :( POR FAVOR ATUALIZAR SUA BIBLIOTECA REQUESTS!! \nDESEJA ATUALIZAR ? [Y/N]")
            		   # atlz = input ("~~~> ")
            		    atlz = input (f"""{az}
┌──({usuario}{P}㉿{G}Termux)-[{P}Shieazs-Black/SHELDRES-SMS{az}]
└─$ +{cdp} """)
            		    print(f" {C}")
            		    if atlz == "Y":
            		        def atualiza():
            		            os.system("pkg install pip -y")
            		            os.system("pip install --upgrade pip")
            		            os.system("pip install requests")
            		            os.system("pip install --upgrade requests")
            		            print(f"{V}[*]Blibliote requests atualizada.\nExecute script novamente.")
            		            exit ()
            		        atualiza()
            		    elif atlz == "N":
            		        def nao_atualiza():
            		            print (f"{G}="*36)
            		            print ("Por favor, se você for usa essa programa  precisa ser atualizado :(")
            		            print("saindo do programa...")
            		            exit ()
            		        nao_atualiza()
            		        
            		print(resp.json ())
            		print(f'{VM}Obrigado por testa Sheldres-sms, Você só podera enviar outro sms após 24horas :)')
            		print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n[ 00 ] ~> Sai do programa.")
            		sleep (3)
            		break
            		print ("MENSAGEM ENVIADA COM SUCESSO! ")
            		if '"success" : true 'in resp.text:
            		    print(f"{V}mensagem enviada com susseso!")
            		    
            		print(f"{P}ERRO SUA MENSAGEM NÃO FOI ENVIADA! :(")
            		if '"success" : false ' in resp.text:
            		    print(f"{VM}Vish deu ruin em algo")
            		    print(f"\{VM} Falha no envio ")
            		    input('presione enter para sair')
            		    banner()
            		    exit()
            		exit() 
        sheldres_sms()
    elif opcao =="c":
        def distribuicoes():
            os.system("clear")
            distro = open("Imgs/distribuicoes")
            print(distro.read ())
            op_distro = input (f"""{C}
┌──({usuario}{P}㉿{G}Termux)-[{P}Shields-Black/distribuições{C}]
└─$ """)
            
            if op_distro == "1":
                def kali_linux():
                    os.system("apt update -y")
                    os.system("pkg upgrade -y")
                    os.system("pkg install wget -y")
                    os.system("pkg install wget proot -y && wget https://raw.githubusercontent.com/MasterDevX/KaliTermux/master/InstallKali.sh && bash InstallKali.sh")
                    os.system("mv InstallKali.sh /data/data/com.termux/files/home")
                    os.system("mv kali-binds /data/data/com.termux/files/home")
                    os.system("mv start-kali.sh /data/data/com.termux/files/home")
                    os.system ("mv kali-fs /data/data/com.termux/files/home")
                    print(f"{P}Instalação concluída...");timeout(3);
                    print("~"*27)
                    print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 90 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
                kali_linux()
                    
            elif op_distro == "2":
                def debian():
                    os.system("curl --silent --location --remote-name https://raw.githubusercontent.com/trungtai33/debian-bullseye-in-termux/master/install.sh; bash install.sh; rm install.sh")
                    print(f"{P}Instalação concluída...");timeout(3);
                    print("~"*27)
                    print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 91 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
                debian()
            
            elif op_distro == "3":
                def ubuntu():
                    os.system("apt-get update -y")
                    os.system("apt-get upgrade -y")
                    os.system("apt-get install wget -y")
                    os.system("apt-get install proot -y")
                    os.system("apt-get install git -y")
                    os.system("git clone https://github.com/MFDGaming/ubuntu-in-termux.git")
                    os.system(" mv ubuntu-in-termux /data/data/com.termux/files/home")
                    print(f"{P}Instalação concluída...");timeout(3);
                    print("~"*27)
                    print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 91 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
                ubuntu()
            
            elif op_distro == "4":
                def hydra():
                    os.system("apt-get update -y")
                    os.system("apt-get upgrade -y")
                    os.system("apt install hydra -y")
                    print(f"{P}Instalação concluída...");timeout(3);
                    print("~"*27)
                    print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 91 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
                hydra()
            
            elif op_distro == "5":
                def arch_linux():
                    os.system("apt-get update -y")
                    os.system("apt-get upgrade -y")
                    os.system("apt-get install bsdtar wget proot tergent tmux openssh")
                    os.system("termux-setup-storage")
                    os.system("apt-get install wget -y")
                    os.system("wget https://raw.githubusercontent.com/SDRausty/termux-arch/master/setupTermuxArch.bash")
                    os.system("mv setupTermuxArch.bash /data/data/com.termux/files/home")
                    print(f"""dicas:
{P} Você vai querer mudar a senha e talvez até o nome de usuário do seu novo usuário Linux.

comando de troca do nome do usuario:
                    {C} user: useradd -mG root -s /bin/bash <Nick>
                     
        {P}  para senha:
                     {C}user: passwd <senha>
                        """)
                    print(f"{P}Instalação concluída...");timeout(3);
                    print("~"*27)
                    print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n{H}[ 91 ] ~> Para voltar ao menu anterior. \n{P}[ 00 ] ~> Sai do programa.")
                arch_linux()
            
            
            
            
            elif op_distro == "99":
                def menu_principal():
                    print(f"{G}Voltando ao menu Inicial...");timeout(1);
                    os.system("clear")
                    menu()
                menu_principal()
            
            elif op_distro == "00":
                def sair():
                    os.system("clear")
                    sair_do_programar()
                    print("SAINDO DO PROGRAMAR....");timeout(3);
                    exit()
                sair()
                
            else:
                print("~"*25)
                print(f"{P}Opção Inválida, escolhar somenter as Opção do menu.:(");timeout(3);
                print(f"{C}~"*25)
                os.system ("clear")
                distribuicoes()
                
        distribuicoes()
    
    elif opcao =="d":
    	def configura():
    		os.system("figlet -f Varsity Começando")
    		os.system("apt update -y")
    		os.system("pkg upgrade -y")
    		print(f"{P}[*] iniciando instalações de pacotes....")
    		sleep (2)
    		print (f"{C}")
    		os.system("pkg install figlet -y")
    		os.system("pkg install python -y")
    		os.system("pkg install python2 -y")
    		os.system("pkg install nano -y")
    		os.system("pkg install curl -y")
    		os.system("pkg install pip -y")
    		os.system("pkg install vim -y")
    		os.system("pkg install git -y")
    		os.system("pkg install wget -y")
    		os.system("pkg install ruby -y")
    		os.system("pkg install sl -y")
    		os.system("pkg install php -y")
    		os.system("pkg install binutils -y")
    		os.system("pkg install man -y")
    		os.system("pkg install perl -y")
    		os.system("pkg install netcat -y")
    		os.system("figlet -f Varsity completo")
    		print(f"{H}[ 99 ] ~> Para voltar ao menu Inicial.\n[ 00 ] ~> Sai do programa.")
    	configura()

    elif opcao == "90":
        def menu_anterior():
            print(f"{G}Voltando ao menu anterior...");timeout(1);
            os.system("clear")
            Packs()
            
        menu_anterior()
    
    elif opcao == "91":
        distribuicoes()
        
    elif opcao == "00":
        def sair():
            os.system("clear")
            sair_do_programar()
            print("SAINDO DO PROGRAMAR....");timeout(2);
            exit()
        sair()
                             
    elif opcao == "99":
        print(f"{G}Voltando ao menu Inicial...");timeout(2);
        os.system("clear")
        menu()
                               
    else:
        print("~"*25)
        print(f"{P}Opção Inválida :(");timeout(3);
        print(f"{C}~"*25)
        os.system ("clear")
        menu()

