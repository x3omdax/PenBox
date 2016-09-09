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

class Variables:
    """
    """
    def __init__(self):
        """
        """
        self.DIRECTORIES = [
        '/uploads/','/upload/','/files/','/resume/','/resumes/','/documents/',\
        '/docs/','/pictures/','/file/','/Upload/','/Uploads/','/Resume/',\
        '/Resume/','/UsersFiles/','/Usersiles/','/usersFiles/','/Users_Files/',\
        '/UploadedFiles/','/Uploaded_Files/','/uploadedfiles/','/uploadedFiles/',\
        '/hpage/','/admin/upload/','/admin/uploads/','/admin/resume/',\
        '/admin/resumes/','/admin/pictures/','/pics/','/photos/',\
        '/Alumni_Photos/','/alumni_photos/','/AlumniPhotos/','/users/'
        ]

        self.SHELLS = [
        'wso.php','shell.php','an.php','hacker.php','lol.php','up.php','cp.php',\
        'upload.php','sh.php','pk.php','mad.php','x00x.php','worm.php',\
        '1337worm.php','config.php','x.php','haha.php'
        ]

        self.UPLOAD = []

        self.YES = ['yes','y', 'ye', 'Y']

        self.NO = ['no','n']

        self.DITECT = ['13', '14', '15', '16', '17', '18', '19', '20', '21']

    def logo(self):
        print("""
     ____            ____
    |  _ \ ___ _ __ | __ )  _____  __
    | |_) / _ \ '_ \|  _ \ / _ \ \/ /
    |  __/  __/ | | | |_) | (_) >  <
    |_|   \___|_| |_|____/ \___/_/\_\V2.4
                             A Penetration Testing Framework


    [+]       Coded BY Mohamed Nour & Fedy Wesleti       [+]
    [+]         FB/mohamed.zeus.0   ~~ FB/CEH.tN         [+]
    [+]             Improved by: Chiheb Nexus            [+]
    [+]                  FB/chihebnexuss                 [+]
    [+]             Greetz To All Pentesters             [+]

    """)

# Test
if __name__ == '__main__':
    app = Variables()
    print(app.DIRECTORIES)
    app.logo()
