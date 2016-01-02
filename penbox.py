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
    print("This Tool Is Made By Fedy wesleti And Mohamed Nour ")
    print("Contact Us facebook.com/CEH.TN , facebook.com/mohamed.zeus.0")
    print("")
    print("this tool will only download and install tools")
    print("and then they will be accesible direcly via command")
    print("")
    print("choose a categorie")
    print("")
    print("1 : information gathering")
    print("2 : password attacks")
    print("3 : wireless attacks")
    print("4 : exploitation tools")
    print("5 : sniffing / spoofing")
    print("6 : exit ")
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
    elif choice == 6:
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

#information gathering function
def info():
    print("1 :nmap (it will install )")
    print("99 :Go Back To Main Menu")
    choice2 = input("selet a number :")
    choice2 = int(choice2)
    if choice2 ==1:
        print nmap()
#end of menu 
##########################
#password attacks menu 
def passwd():
    print("1 :ban ")
    choice3 = input("selet a number :")
    choice3 = int(choice3)
    if choice3 ==1:
     os.system("ls -la")
#end of menu 
##########################
#wireless attacks
def wire():
    print("1 :fan ")
    choice4 = input("selet a number :")
    choice4 = int(choice4)
    if choice4 ==1:
     os.system("ls -la")
##########################
#exploitation tools
def exp():
    print("1 :wan ")
    choice5 = input("selet a number :")
    choice5 = int(choice5)
    if choice5 ==1:
     os.system("ls -la")
###########################
#sniffing tools
def snif():
    print("1 :man ")
    choice6 = input("selet a number :")
    choice6 = int(choice6)
    if choice6 ==1:
     os.system("ls -la")
#end of menu 
##########################
print menu() #show the main menu 
    
    
    
    
  
