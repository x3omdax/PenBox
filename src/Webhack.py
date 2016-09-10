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
from urllib.request import urlopen
from urllib.parse import urlparse
from re import findall
from src.var.MyDecorators import CheckDirectory, CheckFile

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
                Webhack.drupal(self)
                break
            elif user_input == '2':
                pass
            elif user_input == '3':
                pass
            elif user_input == '99':
                break
            else:
                user_input = input("Please enter a number between [1..3] or 99 to back to the previous menu: ")

    def load_url(self, url = None):
        """
        """
        response = urlopen(url)
        return response.read()

    def drupal(self):
        """
        """
        ip_target = input("Enter Target IP Address: ")
        page = 1
        while page <= 50:
            print("Testing page n°: ", page)
            url = "http://www.bing.com/search?q=ip%3A"+ip_target+"&go=Valider&qs=n&form=QBRE&pq=ip%3A"+\
            ip_target+"&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first="+str(page)
            data = Webhack.load_url(self, url)
            filtred_data = findall('<div class="b_title"><h2><a href="(.*?)" h='.encode(), data)
            page +=1
            #print("data: ", data)
            #print("filtred_data: ", filtred_data)

            for urls in filtred_data:
                parsed = urlparse(urls)
                site = parsed.netloc

                print("[+] Testing website: {0}".format(site))
                testing_data = Webhack.load_url(self, site)
                if "User : HolaKo" in testing_data:
                    print("[-] Exploit found in {0}".format(site))
                    print("User: HolaKo\nPass: admin")
                else:
                    print("[-] Exploit not found ! ")


    @CheckDirectory(path = getcwd() + "/src/bin/SCANNER-INURLBR")
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
