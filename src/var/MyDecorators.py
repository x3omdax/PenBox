#!/usr/bin/python3

from os.path import isdir, isfile
from os import system

class CheckDirectory(object):
    def __init__(self, path = None):
        self.path = path

    def __call__(self, f):
        def check_dir(*args):
            #print("isdir: ",isdir(self.path))
            if isdir(self.path):
                print("[-] Directory {0} exist! ".format(self.path.split("/")[-1]))
                user_input = input("Do you want to override it ? [Y/N]: ")
                while True:
                    if user_input == 'Y' or user_input == 'y':
                        print("[-] Deleting {0}".format(self.path))
                        system("sudo rm -r {0}".format(self.path))
                        f(*args)
                        break
                    elif user_input == 'N' or user_input == 'n':
                        break
                    else:
                        user_input = input("Please enter 'Y' or 'N': ")
            else:
                f(*args)
        return check_dir

class CheckFile(object):
    def __init__(self, path = None):
        self.path_file = path

    def __call__(self, f):
        def check_file(*args):
            if isfile(self.path_file):
                print("[-] File {0} exist!".format(self.path_file.split("/")[-1]))
                user_input = input("Do you want to override it ? [Y/N]: ")
                while True:
                    if user_input == 'Y' or user_input == 'y':
                        print("[-] Deleting {0}".format(self.path_file))
                        system("rm {0}".format(self.path_file))
                        f(*args)
                        break
                    elif user_input == 'N' or user_input == 'n':
                        break
                    else:
                        user_input = input("Please enter 'Y' or 'N'")
            else:
                f(*args)
        return check_file
