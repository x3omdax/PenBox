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

class Sn1per:
    """
    """
    def __init__(self):
        """
        """
        print("[+] Checking if Sn1per exist in the current OS ...")
        # Check if sniper exist in the current OS
        status = system("which sniper")
        if status == '0':
            print("[-] Sn1per exist!")
            try:
                system("sniper")
            except Exception as e:
                print("Error occured during the execution", e)
        else:
            print("[-] Sn1per didn't exist ... ")
            # System must have git installed before excecuting this command
            print("[+] Cloning Sn1per from Github to {0} ...".format(getcwd() + "/src/bin"))
            system("cd src/bin/ && git clone https://github.com/1N3/Sn1per.git")
            print("[-] Done.")
            # Running the installation script
            print("[+] Installing Sn1per ...")
            system("cd src/bin/ && cd Sn1per && bash ./install.sh")
            try:
                system("sniper")
            except Exception as e:
                print("Error occured during the execution ", e)

# Testing
if __name__ == '__main__':
    app = Sn1per()
