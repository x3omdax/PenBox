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

class Passwd:
    """
    """
    def __init__(self):
        self.DIRECTORY = getcwd() + "/src/bin"

    def cupp(self):
        """
        """
        print("Cupp is a password list generator")
        print("[+] Cloning Cupp from github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/Mebus/cupp.git")

    def ncrack(self):
        """
        """
        print("Ncrack is a network authentication cracking tool developed using Ruby")
        print("[+] Cloning Ncrack from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/sophsec/ruby-ncrack.git")
        print("[+] Checking/Installing Dependencies on Ubuntu OS ...")
        system("sudo apt-get install ruby-full")
        print("[+] Checking/Installing ncrack ...")
        system("gem install ruby-ncrack")
