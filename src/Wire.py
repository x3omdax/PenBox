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

class Wire:
    """
    """
    def __init__(self):
        self.DIRECTORY = getcwd() + "/src/bin/reaver-wps-fork-t6x"

    @CheckDirectory(path = getcwd() + "/src/bin/reaver-wps-fork-t6x")
    def reaver(self):
        """
        """
        print("""
        Reaver has been designed to be a robust and practical attack against Wi-Fi Protected Setup
        WPS registrar PINs in order to recover WPA/WPA2 passphrases. It has been tested against a
        wide variety of access points and WPS implementations
        1 to accept / 0 to decline
        """)
        print("[+] Checking/Installing Dependencies on Debian based OS ...")
        system("sudo apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps")
        print("[+] Cloning Reaver from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/t6x/reaver-wps-fork-t6x.git")
        print("[+] Configuring downloaded packages ...")
        system("cd src/bin/reaver-wps-fork-t6x/src && ./configure && make && sudo make install")

    @CheckDirectory(path = getcwd() + "/src/bin/pixiewps")
    def pixiewps(self):
        """
        """
        print("""
        Pixiewps is a tool written in C used to bruteforce offline the WPS pin exploiting the low
        or non-existing entropy of some Access Points, the so-called "pixie dust attack" discovered by
        Dominique Bongard in summer 2014. It is meant for educational purposes only
        """)

        print("[+] Cloning Piwiewps from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/wiire/pixiewps.git")
        print("[+] Checking/Installing Dependencies on Debien based OS ...")
        system("sudo apt-get -y install build-essential")
        print("[+] Installing Piwiewps ...")
        system("cd src/bin/ && make && sudo make install")

    @CheckFile(path = getcwd() + "/src/bin/bluepot-0.1.tar.gz")
    def bluepot(self):
        """
        """
        print("""
        you need to have at least 1 bluetooh receiver (if you have many it will work wiht those, too).
        You must install / libbluetooth-dev on Ubuntu / bluez-libs-devel on Fedora/bluez-devel on openSUSE.
        You need also to have Java or OpenJDK installed on your system in order to run Bluepot
        """)

        print("[+] Downloading Bluepot from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && wget https://github.com/andrewmichaelsmith/bluepot/raw/master/bin/bluepot-0.1.tar.gz")
        print("[+] Checking/Installation Dependencies on Ubuntu OS ...")
        system("sudo apt-get install libbluetooth-dev")
        print("[+] Extracting Bluepot tar.gz file ...")
        system("cd src/bin/ && tar xzvf bluepot-0.1.tar.gz")
        system("cd src/bin/bluepot/ && sudo java -jar BluePot-0.1.jar")
