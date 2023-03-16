
#Code source: https://github.com/plonxyz/VThash-checker/blob/master/vt-check.py

import requests
import csv
import json
import time
import hashlib
import sys
import argparse

def checkHashes(api_key, dirhash): #function for checking txt-file with multiple hashes
  tobehashed = ".\hashes.txt"
  path = "result.txt"
  i = (int(len(dirhash))) - 1
  with open(tobehashed, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        stack = []
        line=1
        for line in csv_reader:
            print("Importing Hash {} into Stack".format(line))
            stack.append(line)
        newfile= open(path, 'a')
        while stack:
          gethash=stack.pop()
          gethash=( ", ".join( str(e) for e in gethash ) )
          x=printResult(gethash, api_key)
          newfile.write("Name: {} \nSHA256: {} \nLast scanned: {} \nScore:{}/{} \nLink.: {} \n\n" .format(dirhash[i][0],x.get('sha256'),x.get('scan_date'),x.get('positives'),x.get('total'),x.get('permalink')))
          i = i -1
          if len(stack) > 0 :
            progressBar()
        newfile.close()
        print("\nDONE, CHECK YOUR RESULTS AT '{}'".format(path))


def vtGetResults(hashes, api_key):
  headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent" : "gzip,  My Python requests library example client or username"
    }
  params = {'apikey': api_key , 'resource':hashes}
  response = requests.post('https://www.virustotal.com/vtapi/v2/file/report', params=params , headers=headers)
  json_response = response.json()

  return json_response

def printResult(hash, api_key):
  getresult = vtGetResults(hash, api_key)
  print("\nSHA256 HASH:{}" .format(getresult.get('sha256')))
  print("Last scanned: {}" .format(getresult.get('scan_date')))
  print("Score:{}/{}".format(getresult.get('positives'),getresult.get('total')))
  print("Link.: {} \n".format(getresult.get('permalink') ))
  return getresult


def progressBar():
  toolbar_width = 30
  print("____________________________________________\n")
  print("Waiting 15 Sec. to prevent free API timeout\n")
  print("____________________________________________\n")
  sys.stdout.write("[%s]" % (" " * toolbar_width))
  sys.stdout.flush()
  sys.stdout.write("\b" * (toolbar_width+1)) 
  for i in range(toolbar_width):
      time.sleep(0.5) 
      sys.stdout.write("-")
      sys.stdout.flush()
  sys.stdout.write("\n")
  
   


