# Christian Piper
# 11/11/19
# This program will upload the project to github

import os

def main():
    versionName = input("Input the commit name: ")
    os.system("git add *")
    os.system("git commit -m '" + versionName + "'")
    os.system("git push")

main()