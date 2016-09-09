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

class Webhack:
    """
        @FIXME
    """
    def __init__(self):
        self.DIRECTORY = getcwd() + "/src/bin"

    def drupal_main(self):
        """
            @FIXME
        """
        print("""
        1- Drupal
        2- Get Drupal
        3- Drupal list
        99- Back to the previous menu
        """)
        user_input = input("Enter a number: ")
        while True:
            if user_input == '1':
                pass
            elif user_input == '2':
                pass
            elif user_input == '3':
                pass
            elif user_input == '99':
                break
            else:
                user_input = input("Please enter a number between [1..3] or 99 to back to the previous menu: ")

    def inurlbr(self):
        """
        """
        print("""
        Advanced search in search engines, enables analysis provided to exploit GET / POST capturing emails & urls,
         with an internal custom validation junction for each target / url found.
        """)

        print("[+] Checking/Installing Dependencies on Debian based OS ...")
        system("sudo apt-get install curl libcurl3 libcurl3-dev php5 php5-cli php5-curl")
        print("[+] Cloning InURLbr from Github to {0} ...".format(self.DIRECTORY))
        system("cd src/bin && git clone https://github.com/googleinurl/SCANNER-INURLBR.git")
