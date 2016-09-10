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
from src.var.MyDecorators import CheckDirectory, CheckFile

class Snif:
    """
    """
    def __init__(self):
        self.DIRECTORY = getcwd() + "/src/bin"

    @CheckDirectory(path = getcwd() + "/src/bin/social-engineer-toolkit")
    def setoolkit(self):
        """
        """
        print("""
        The Social-Engineer Toolkit is an open-source penetration testing framework
        designed for social engineering. SET has a number of custom attack vectors that
        allow you to make a believable attack quickly. SET is a product of TrustedSec, LLC
        an information security consulting firm located in Cleveland, Ohio.
        """)

        print("[+] Cloning Setoolkit from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/trustedsec/social-engineer-toolkit.git")

    @CheckDirectory(path = getcwd() + "/src/bin/sslstrip")
    def ssls(self):
        """
        """
        print("""
        sslstrip is a MITM tool that implements Moxie Marlinspike's SSL stripping
        attacks. It requires Python 2.5 or newer, along with the 'twisted' python module.
        """)
        print("[+] Checking/Installing Dependencies on Debian based OS ...")
        system("sudo apt-get install python-twisted-web")
        print("[+] Cloning SSLStrip from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/moxie0/sslstrip.git")

    @CheckFile(path = getcwd() + "/src/bin/pisher.py" )
    def pisher(self):
        """
        """
        print("[+] Downloading Pisher from Pastebin to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && wget http://pastebin.com/raw/DDVqWp4Z --output-document=pisher.py")

    @CheckFile(path = getcwd() + "/src/bin/smtpsend.py")
    def smtpsend(self):
        """
        """
        print("[+] Downloading SMTPsend from Pastebin to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && wget http://pastebin.com/raw/Nz1GzWDS --output-document=smtpsend.py")
