#!/usr/bin/python3
#
#  PenBox: A Penetration Testing Framework , The Hacker’s Repo
#
#    [+]       Coded BY Mohamed Nour & Fedy Wesleti       [+]
#    [+]         FB/mohamed.zeus.0   ~~ FB/CEH.tN         [+]
#    [+]             Improved by: Chiheb Nexus            [+]
#    [+]                  FB/chihebnexuss                 [+]
#    [+]             Greetz To All Pentesters             [+]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
################################################################################
################################# Main #########################################

from sys import version_info, exit
if version_info.major < 3:
    print("This script require Python v3 or newer versions\nExit ...")
    exit()
from src.var.Variables import Variables
from src.Sn1per import Sn1per
from src.Info import Info
from src.Passwd import Passwd
from src.Wire import Wire
from src.Exp import Exp
from src.Snif import Snif
from src.Webhack import Webhack
from src.PostExploit import PostExploit
from os import system

class PenBox:
    """
        Main class
    """
    def __init__(self):
        """
            initialise all sub classes
        """
        # initialise Variables class
        Variables.__init__(self)
        self._ = Variables()

        # initialise Info class
        Info.__init__(self)

        # initialise Passwd class
        Passwd.__init__(self)

        # initialise Wire class
        Wire.__init__(self)

        # initialise Exp class
        Exp.__init__(self)

        # initialise Snif class
        Snif.__init__(self)

        # initialise Webhack class
        Webhack.__init__(self)

        # initialise PostExploit class
        PostExploit.__init__(self)

    def main(self):
        """
            The core of the script
        """
        self._.logo()
        input("Press any key to continue ...")

        print("""
        Select from the menu:
        1 : Information Gathering
        2 : Password Attacks
        3 : Wireless Testing
        4 : Exploitation Tools
        5 : Sniffing & Spoofing
        6 : Web Hacking
        7 : Private Tools
        8 : Post Exploitation
        9 : Recon
        99: Exit\n""")

        user_input = input("Please enter a number: ")

        while True:
            if user_input == '1':
                Info.__init__(self)
                print("""
        1- Nmap
        2- Setoolkit
        3- Port Scanning
        4- Host to IP
        5- Wordpress user enumeration
        6- CMS Scanner
        7- XSStracer - checks remote web servers for Clickjacking, Cross-Frame Scripting, \
Cross-Site Tracing and Host Header Injection
        8- Doork - Google Dorks Passive Vulnerability Auditor
        9- Scan A server's Users
        99- Back To Main Menu
                """)
                user_input2 = input("Enter a number: ")
                while True:
                    if user_input2 == '1':
                        Info.nmap(self)
                        break
                    elif user_input2 == '2':
                        Info.setoolkit(self)
                        break
                    elif user_input2 == '3':
                        Info.ports(self)
                        break
                    elif user_input2 == '4':
                        Info.h2ip(self)
                        break
                    elif user_input2 == '5':
                        Info.wpue(self)
                        break
                    elif user_input2 == '6':
                        Info.cmsscan(self)
                        break
                    elif user_input2 == '7':
                        Info.xsstracer(self)
                        break
                    elif user_input2 == '8':
                        Info.doork(self)
                        break
                    elif user_input2 == '9':
                        Info.scanusers(self)
                        break
                    elif user_input2 == '99':
                        self.main()
                    else:
                        user_input2 = input("Please enter a valid number between [1..9] or 99 to back to the main menu: ")
            elif user_input == '2':
                print("""
        1- Cupp
        2- Ncrack
        99- Back to main menu
                """)
                user_input3 = input("Enter a number: ")
                while True:
                    if user_input3 == '1':
                        Passwd.cupp(self)
                        break
                    if user_input3 == '2':
                        Passwd.ncrack(self)
                        break
                    if user_input3 == '99':
                        self.main()
                    else:
                        user_input3 = input("Please enter a valid number between [1,2] or 99 to back to main menu: ")
            elif user_input == '3':
                print("""
        1- Reaver
        2- Pixiewps
        3- Bluetooth Honeypot Gui Framework
        99- Back to main menu
                """)
                user_input4 = input("Enter a number: ")
                while True:
                    if user_input4 == '1':
                        Wire.reaver(self)
                        break
                    elif user_input4 == '2':
                        Wire.pixiewps(self)
                        break
                    elif user_input4 == '3':
                        Wire.bluepot(self)
                        break
                    elif user_input4 == '99':
                        self.main()
                    else:
                        user_input4 = input("Please enter a valid number between [1..3] or 99 to back to the main menu: ")
            elif user_input == '4':
                print("""
        1- Venom
        2- SQLmap
        3- Shellnoob
        4- Commix
        5- FTP Auto Bypass
        6- Jboss-autopwn
        7- Blind SQL Automatic Injection and Exploit
        8- Brutefoce Android Passcode (AndroidPINCrack)
        9- Joomla, Mambo, PHP-Nuke, and XOOPS CMS SQL injection Scanner
        99- Back to the main menu
                """)
                user_input5 = input("Enter a number: ")
                while True:
                    if user_input5 == '1':
                        Exp.venom(self)
                        break
                    elif user_input5 == '2':
                        Exp.sqlmap(self)
                        break
                    elif user_input5 == '3':
                        Exp.shellnoob(self)
                        break
                    elif user_input5 == '4':
                        Exp.commix(self)
                        break
                    elif user_input5 == '5':
                        Exp.gabriel(self)
                        break
                    elif user_input5 == '6':
                        Exp.jboss(self)
                        break
                    elif user_input5 == '7':
                        Exp.bsqlbf(self)
                        break
                    elif user_input5 == '8':
                        Exp.androidhash(self)
                        break
                    elif user_input5 == '9':
                        Exp.cmsfew(self)
                        break
                    elif user_input5 == '99':
                        self.main()
                    else:
                        user_input5 = input("Please enter a number between [1..9] or 99 to back to the main meun: ")
            elif user_input == '5':
                print("""
        1- Setoolkit
        2- SSLTrip
        3- pyPisher
        4- SMTP Mailer
        99- Back to main menu
                """)
                user_input6 = input("Enter a number: ")
                while True:
                    if user_input6 == '1':
                        Snif.setoolkit(self)
                        break
                    elif user_input6 == '2':
                        Snif.ssls(self)
                        break
                    elif user_input6 == '3':
                        Snif.pisher(self)
                        break
                    elif user_input6 == '4':
                        Snif.smtpsend(self)
                        break
                    elif user_input6 == '99':
                        self.main()
                    else:
                        user_input6 = input("Please enter a number between [1..4] of 99 to back to the main menu: ")
            elif user_input == '6':
                print("""
        1- Drupal
        2- Inurlbr
        3- Wordpress & Joomla Scanner
        4- Gravity Form Scanner
        5- File Upload Checker
        6- Wordpress Exploit Scanner
        7- Wordpress Plugins Scanner
        8- Shell and Directory Finder
        9- Joomla! 1.5 - 3.4.5 remote code execution
        10- Vbulletin 5.X remote code execution
        11- BruteX - Automatically brute force all services running on a target
        12- Arachni - Web Application Security Scanner Framework
        13- Sub-domain Scanning
        14- Wordpress Scanning
        15- Wordpress Username Enumeration
        16- Wordpress Backup Grabbing
        17- Sensitive File Detection
        18- Same-Site Scripting Scanning
        19- Click Jacking Detection
        20- Powerful XSS vulnerability scanning
        21- SQL Injection vulnerability scanning
        99- Back to the main menu
                """)
                user_input7 = input("Enter a number: ")
                while True:
                    if user_input7 == '1':
                        Webhack.drupal_main(self)
                        break
                    elif user_input7 == '2':
                        Webhack.inurlbr(self)
                        break
                    elif user_input7 == '3':
                        print("@FIXME")
                        break
                    elif user_input7 == '4':
                        print("@FIXME")
                        break
                    elif user_input7 == '5':
                        print("@FIXME")
                        break
                    elif user_input7 == '6':
                        print("@FIXME")
                        break
                    elif user_input7 == '7':
                        print("@FIXME")
                        break
                    elif user_input7 == '8':
                        print("@FIXME")
                        break
                    elif user_input7 == '9':
                        print("@FIXME")
                        break
                    elif user_input7 == '10':
                        print("@FIXME")
                        break
                    elif user_input7 == '11':
                        print("@FIXME")
                        break
                    elif user_input7 == '12':
                        print("@FIXME")
                        break
                    elif user_input7 == '13':
                        print("@FIXME")
                        break
                    elif user_input7 == '14':
                        print("@FIXME")
                        break
                    elif user_input7 == '15':
                        print("@FIXME")
                        break
                    elif user_input7 == '16':
                        print("@FIXME")
                        break
                    elif user_input7 == '17':
                        pass
                    elif user_input7 == '18':
                        print("@FIXME")
                        break
                    elif user_input7 == '19':
                        print("@FIXME")
                        break
                    elif user_input7 == '20':
                        print("@FIXME")
                        break
                    elif user_input7 == '21':
                        print("@FIXME")
                        break
                    elif user_input7 == '99':
                        self.main()
                    else:
                        user_input7 == input("Please enter a number between [1..21] or 99 to back to the main menu: ")
            elif user_input == '7':
                print("\t@FIXEME")
                break
            elif user_input == '8':
                print("""
        1- Shell Checker
        2- POET - Post-Exploitation Tool
        3- Weeman - Phishing Framework
        99- Back to the main menu
                """)
                user_input8 = input("Enter a number: ")
                while True:
                    if user_input8 == '1':
                        PostExploit.sitechecker(self)
                        break
                    elif user_input8 == '2':
                        PostExploit.poet(self)
                        break
                    elif user_input8 == '3':
                        PostExploit.weeman(self)
                        break
                    elif user_input8 == '99':
                        self.main()
                    else:
                        user_input8 = input("Enter a valid number between [1..3] or 99 to back to the main menu: ")
            elif user_input == '9':
                # initialise Sn1per class
                Sn1per.__init__(self)
                break
            elif user_input == '99':
                print("Exit...")
                exit()
            else:
                user_input = input("Please enter a valid number between [1..9] or 99 to exit this script: ")


# Run the BEAST !
if __name__ == '__main__':
    app = PenBox()
    app.main()
