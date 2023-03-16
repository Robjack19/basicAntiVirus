#!/usr/bin/env python 
from fileCleaner import cleanerNpacker
from vtCheck import checkHashes
from htmlMaker import maker
import subprocess
import webbrowser
import time

#api key check
choice = (input("Use new api key?(Y/N)"))
choice = choice.upper()

#adding new key
if choice == 'Y':
    new_key = input("Enter new api key.")
    file = open("vtapikey.txt","w")
    file.write(new_key)
    file.close()
    print("\n")

elif choice == 'N':
    print("Using old key...")
   
else:
    print("Invalid response")
    exit()

#get api key
file = open("vtapikey.txt","r")
api_key = file.read()
file.close()
time.sleep(0.5)

#executing 'getDirHash.bat'
print("Collecting file names and hashes...")
subprocess.call([r'.\getDirHash.bat'])
time.sleep(0.5)

#get tuple
print("Creating tuple in [(file_name:file_hash)] format...")
dirNhash = cleanerNpacker()
time.sleep(0.5)

#chech VirusTotal
print("Checking VirusTotal...")
file = open('hashes.txt','w')
for i in range(len(dirNhash)):
    file.write(dirNhash[i][1]+'\n')
file.close()

checkHashes(api_key, dirNhash)
time.sleep(0.5)

#delete files
print("Deleting un-necessary files...")
subprocess.call([r'.\delfiles.bat'])
time.sleep(0.5)

#create result.html
print("Creating .html file")
maker()
time.sleep(0.5)

#run result.html
url = "result.html"
webbrowser.open(url, new=2)

exit()