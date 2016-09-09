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

from os import system, getcwd

class Info:
    """
    """
    def __init__(self):
        self.DIRECTORY = getcwd() + "/src/bin"

    def nmap(self):
        """
        """
        print("[+] Checking if Nmap exist in the current OS ... ")
        status = system("which nmap")
        if status == '0':
            print("[-] Nmap exist!")
        else:
            print("[-] Nmap didn't exist ...")
            print("[+] Downloading Nmap to {0} ...".format(self.DIRECTORY))
            system("cd src/bin/ && wget https://nmap.org/dist/nmap-7.01.tar.bz2")
            system("cd src/bin/ && tar xjf nmap-7.01.tar.bz2")
            system("cd src/bin/nmap-7.01/ && ./configure && make && make install")
            print("[+] Cleaning ...")
            system("rm -r src/bin/nmap-7.01 && rm src/bin/nmap-7.01.tar.bz2")
            print("[-] Done.")

    def setoolkit(self):
        """
        """
        print("[+] Checking if Setoolkit exist in the current OS ...")
        status = system("which setoolkit")
        if status == '0':
            print("[-] setoolkit exist!")
        else:
            print("[-] setoolkit didn't exist ...")
            print("[+] Cloning setoolkit from Github to {0} ...".format(self.DIRECTORY))
            ll = system("cd src/bin/ && git clone https://github.com/trustedsec/social-engineer-toolkit.git")
            print("[-] Cloning done ...")
            print("[+] Installing setoolkit ...")
            try:
                system("cd src/bin/social-engineer-toolkit/ && python setup.py")
            except Exception as e:
                print("[-] Installation interrupted ", e)

    def ports(self):
        """
        """
        target = input("Enter Target IP address: ")
        system("nmap nmap -O -Pn {0}".format(target))
        input("Enter space to continue ...")

    def h2ip(self):
        """
        """
        try:
            from socket import gethostbyname
        except Exception as e:
            print("Cannot import gethostbyname ...\nExit...")
            from sys import exit
            exit()

        host = input("Enter a Host: ")
        print(gethostbyname(host))
        input("Enter any key to continue ...")

    def wpue(self):
        """
        """
        from platform import dist
        distribution = dist()[0]

        if distribution == "Ubuntu":
            print("[+] Checking/Installing Dependencies on Ubuntu OS...")
            system("sudo apt-get install libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev build-essential libgmp-dev zlib1g-dev")
        elif distribution == "Debian":
            print("[+] Checking/Installing Dependencies on Debian OS...")
            system("sudo apt-get install git ruby ruby-dev libcurl4-openssl-dev make zlib1g-dev")
        elif distribution == "Fedora":
            print("[+] Checking/Installing Dependencies on Fedora OS...")
            system("sudo dnf install gcc ruby-devel libxml2 libxml2-devel libxslt libxslt-devel libcurl-devel patch rpm-build")
        elif distribution == "Arch Linux":
            system("pacman -Syu ruby")
            system("pacman -Syu libyaml")

        print("[-] Done.")
        print("[+] Cloning WPScanTeam from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin/ && git clone https://github.com/wpscanteam/wpscan.git")
        target = input("Enter a Wordpress Target: ")
        system("cd src/bin/wpscan && ruby wpscan.rb --url {0} --enumerate u".format(target))
        input("Enter space to continue ...")

    def cmsscan(self):
        """
        """
        print("[+] Cloning CMSmap from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin/ && git clone https://github.com/Dionach/CMSmap.git")
        target = input("Enter Target: ")
        system("cd src/bin/CMSmap/ && python cmsmap.py -t {0}".format(target))

    def xsstracer(self):
        """
        """
        print("""XSSTracer is a small python script that checks remote web servers for Clickjacking,\
 Cross-Frame Scripting, Cross-Site Tracing and Host Header Injection.""")

        print("[+] Cloning XSSTracer from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/1N3/XSSTracer.git")
        target = input("Enter Target address: ")
        port = input("Enter Target port: ")
        system("cd src/bin/XSSTracer && python xsstracer.py {0} {1}".format(target, port))

    def doork(self):
        """
        """
        print("""doork is a open-source passive vulnerability auditor tool that automates the process of searching on Google\
 information about specific website based on dorks.
        """)
        print("[+] Checking/Installing Dependencies on Ubuntu OS...")
        system("sudo apt-get install pip")
        system("sudo pip install beautifulsoup4 && sudo pip install requests")
        print("[+] Cloning Doork from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin/ && git clone https://github.com/AeonDave/doork.git")
        target = input("Enter Target address: ")
        system("cd src/bin/ && python doork.py -t {0} -o log".format(target))

    def scanusers(self):
        """
            @FIXME
        """
        print("NEED FIX!")
        pass
