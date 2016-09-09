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

class Exp:
    """
    """
    def __init__(self):
        self.DIRECTORY = getcwd() + "/src/bin"

    def venom(self):
        """
        """
        print("Venom is an Automatic ShellCode generator")
        print("[+] Cloning Venom from SourceForge to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone git://git.code.sf.net/p/crisp-shellcode-generator/shell crisp-shellcode-generator-shell")
        print("[+] Checking/Installing Dependencies ...")
        system("cd src/bin/crisp-shellcode-generator-shell && sudo bash venom.sh ")

    def sqlmap(self):
        """
        """
        print("""
        sqlmap is an open source penetration testing tool that automates the process of detecting
        and exploiting SQL injection flaws and taking over of database servers.
        It comes with a powerful detection engine, many niche features for the ultimate penetration tester
        and a broad range of switches lasting from database fingerprinting, over data fetching from the database,
        to accessing the underlying file system and executing commands on the operating system via out-of-band connections.
        """)
        print("[+] Cloning SQLmap from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/sqlmapproject/sqlmap.git")

    def shellnoob(self):
        """"
        """
        print("""
        Writing shellcodes has always been super fun, but some parts are extremely boring and error prone.
        Focus only on the fun part, and use ShellNoob!
        """)
        print("[+] Cloning Shellnoob from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/reyammer/shellnoob.git")

    def commix(self):
        """
        """
        print("""
        Automated All-in-One OS Command Injection and Exploitation Tool.
        """)
        print("[+] Cloning commix from github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/stasinopoulos/commix.git")

    def gabriel(self):
        """
        """
        print("""
        Abusing authentication bypass of Open&Compact (Gabriel's).
        """)
        print("[+] Downloading Gabriel from Pastebin to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && wget http://pastebin.com/raw/Szg20yUh --output-document=gabriel.py ")

    def jboss(self):
        """
        """
        print("""
        This JBoss script deploys a JSP shell on the target JBoss AS server.
        Once deployed, the script uses its upload and command execution capability to
        provide an interactive session.
        """)

        print("[+] Cloning Jboss-autopwn from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/SpiderLabs/jboss-autopwn.git")

    def bsqlbf(self):
        """
        """
        print("""
        This tool will only work on blind sql injection.
        """)
        print("[+] Checking/Installing Dependencies on Debian based OS ...")
        system("sudo apt-get install perl")
        print("[+] Downloading from Google Code Archive to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/bsqlbf-v2/bsqlbf-v2-7.pl")

    def cmsfew(self):
        """
        """
        print("""
        This Python script run only on target using Joomla, Mambo, PHP-Nuke, or/and XOOPS Only.
        """)
        print("[+] Downloading CMSFew from packetstormsecurity.net to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && wget https://dl.packetstormsecurity.net/UNIX/scanners/cms_few.py.txt -O cmsfew.py")

    def androidhash(self):
        """
        """
        print("""
        AndroidPINCrack is a Python script that bruteforce the Android Passcode given the hash and salt.
        Of course there are some other faster ways to crack than a python script,
        but it can be useful for numeric passcoders or wordlist attack.
        """)
        print("[+] Cloning AndroidPINCrack from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/PentesterES/AndroidPINCrack.git")
