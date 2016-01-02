#
#          All In One Tool For Penetration Testing 
#           Authors : Fedy Wesleti , Mohamed Nour 
#
import sys
import os
import subprocess
from commands import *
########################## 
#Variables
yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])



##########################

#this is the big menu funtion 
def menu():
    print ' ########  ######## ##    ## ########   #######  ##     ## '
    print ' ##     ## ##       ###   ## ##     ## ##     ##  ##   ##  '
    print ' ##     ## ##       ####  ## ##     ## ##     ##   ## ##   '
    print ' ########  ######   ## ## ## ########  ##     ##    ###    '
    print ' ##        ##       ##  #### ##     ## ##     ##   ## ##   '
    print ' ##        ##       ##   ### ##     ## ##     ##  ##   ##  '
    print ' ##        ######## ##    ## ########   #######  ##     ##  v1.0  '
    print '                                 Pentesting Tools Auto-Downloader '
    print ''
    print ' [+]       Coded BY Mohamed Nour & Fedy Weslety        [+] '
    print ' [+]          FB/CEH.TN    ~~   FB/mohamed.zeus.0      [+] '
    print ' [+]             Greetz To All Pentesters              [+] '

    print("")
    print("Select from the menu:")
    print("")
    print("1 : Information Gathering")
    print("2 : Password Attacks")
    print("3 : Wireless Testing")
    print("4 : Exploitation Tools")
    print("5 : Sniffing & Spoofing")
    print("6 : Exit ")
    choice = input("selet a number :")
    choice = int(choice)
    if choice == 1:
        print info()
    elif choice == 2:
        print passwd()
    elif choice == 3:
        print wire()
    elif choice == 4:
        print exp()
    elif choice == 5:
        print snif()
    elif choice == 99:
        os.system('clear'),sys.exit();
#end of function
##########################
#nmap function 
def nmap():
    print("this step will download and install nmap ")
    print("1 to accept / 0 to decline")
    choice7 = input("1/0 :")
    choice7 = int(choice7)
    if choice7 ==1:
        os.system("wget https://nmap.org/dist/nmap-7.01.tar.bz2")
        os.system("bzip2 -cd nmap-7.01.tar.bz2 | tar xvf -")
        os.system("cd nmap-7.01")
        os.system("./configure")
        os.system("make")
        os.system("su root")
        os.system("make install")
    elif choice7 ==0:
        print info()
####################################
#jboss-autopwn
def jboss():
    os.system('clear')
    print ("This JBoss script deploys a JSP shell on the target JBoss AS server. Once")
    print ("deployed, the script uses its upload and command execution capability to")
    print ("provide an interactive session.")
    print ("")
    print (" this will install jboss-autopwn") 
    print ("usage : ./e.sh target_ip tcp_port ")
    print("1 to accept / 0 to decline")
    choice9 = input("1/0 :")
    choice9 = int(choice9)
    if choice9 ==1:
        os.system("git clone https://github.com/SpiderLabs/jboss-autopwn.git"),sys.exit();
    elif choice9 ==0:
        os.system('clear');print exp()
#sqlmap 
def sqlmap():
    print (" this will install sqlmap ")
    print ("usage : python sqlmap.py -h")
    print("1 to accept / 0 to decline")
    choice8 = input("1/0 :")
    choice8 = int(choice8)
    if choice8 ==1:
        os.system("git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
    elif choice8 ==0:
        os.system('clear');print info()

#setoolkit 
def setoolkit():
    print ("The Social-Engineer Toolkit is an open-source penetration testing framework")
    print(") designed for social engineering. SET has a number of custom attack vectors that ")
    print(" allow you to make a believable attack quickly. SET is a product of TrustedSec, LLC  ")
    print("an information security consulting firm located in Cleveland, Ohio.")
    print("")
    print("1 to accept / 0 to decline")
    choiceset = input("1/0 :")
    choiceset = int(choiceset)
    if choiceset ==1:
        os.system("git clone https://github.com/trustedsec/social-engineer-toolkit.git");os.system("cd social-engineer-toolkit");os.system("python setup.py")
    if choiceset ==0:
        os.system("clear");print info()
#cupp 
def cupp():
    print("cupp is a password list generator ")
    print("Usage: python cupp.py -h")
    print("1 to accept / 0 to decline")
    choicecupp = input("1/0 :")
    choicecupp= int(choicecupp)
    if choicecupp ==1:
        os.system("git clone https://github.com/Mebus/cupp.git");os.system("cd cupp")
    elif choicecupp ==0:
        os.system("clear");print passwd()
#ncrack 
def ncrack():
    print("A Ruby interface to Ncrack, Network authentication cracking tool.")
    print("requires : nmap >= 0.3ALPHA / rprogram ~> 0.3")
    print("1 to accept / 0 to decline")
    choicencrack = input("1/0 :")
    choicencrack= int(choicencrack)
    if choicencrack==1:
        os.system("git clone https://github.com/sophsec/ruby-ncrack.git");os.system("cd ruby-ncrack");os.systemgem("install ruby-ncrack")
    elif choicencrack==0:
        os.system("clear");print passwd()
#reaver
def reaver():
    print("Reaver has been designed to be a robust and practical attack against Wi-Fi Protected Setup")
    print(" WPS registrar PINs in order to recover WPA/WPA2 passphrases. It has been tested against a")
    print(") wide variety of access points and WPS implementations")
    print("1 to accept / 0 to decline")
    creaver = input("1/0 :")
    creaver = int(creaver)
    if creaver==1:
        os.system("apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps");os.system("git clone https://github.com/t6x/reaver-wps-fork-t6x.git");os.system("cd reaver-wps-fork-t6x");os.system("cd src/");os.system("./configure");os.system("make")
    elif creaver==0:
        os.system("clear");print wire()

#####################################
#information gathering function
def info():
    print("1 :nmap ")
    print("3 :SET tool kit")
    print("99 :Go Back To Main Menu")
    choice2 = input("selet a number :")
    choice2 = int(choice2)
    if choice2 ==1:
        os.system('clear');print nmap()
    if choice2 ==3:
        os.system("clear");print setoolkit()

    elif choice2 ==99:
        os.system("clear");print menu()
#end of menu 
##########################
#password attacks menu 
def passwd():
    print("1 :cupp ")
    print("2 :Ncrack")
    print("99:Back To Main Menu")
    choice3 = input("selet a number :")
    choice3 = int(choice3)
    if choice3 ==1:
     os.system("clear");print cupp()
    elif choice3 ==2:
        os.system("clear");print ncrack()
    elif choice3 ==99:
        os.system("clear") ; print menu()
#end of menu 
##########################
#wireless attacks
def wire():
    print("1 :reaver ")
    print("99: Go Back To The Main Menu")
    choice4 = input("selet a number :")
    choice4 = int(choice4)
    if choice4 ==1:
     os.system("clear");reaver()
    elif choice4 ==99:
        print menu()
##########################
#exploitation tools
def exp():
    print("1 :jboss-autopwn ")
    print("2 :sqlmap")
    print("99 :Go Back To Main Menu")
    choice5 = input("selet a number :")
    choice5 = int(choice5)
    if choice5 ==2:
        os.system("clear");print sqlmap()
    if choice5 ==1:
     os.system('clear');print jboss()
    elif choice5 ==99:
        print menu()
###########################
#sniffing tools
def snif():
    print("1 :Set Tool kit ")
    print("99: Back To Main Menu")
    choice6 = input("selet a number :")
    choice6 = int(choice6)
    if choice6 ==1:
     os.system("clear") ; print setoolkit()
    if choice6 ==99:
       os.system("clear"); print menu()
#end of menu 
##########################
  #Check user ID 
if os.getuid() != 0:
        print("Are you root? Please execute as root")
        exit()
print menu() #show the main menu 
    
    
    
    
  
