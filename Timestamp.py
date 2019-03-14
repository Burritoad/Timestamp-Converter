from sys import argv
from datetime import datetime,timedelta
import csv
 
def timestamp(stampString):
 minDate = datetime(1990, 1, 1)
 maxDate = datetime(2020, 1, 1)
 final = stampString
 
 try: #try to cast to int
  result = int(stampString)
 except ValueError: #try hex format
  try:
   result = int(stampString, 16)
  except ValueError: #try weird MS format
   try:
    result = int("".join(stampString.split()[::-1]), 16)
   except:
    result = "cannot resolve"
 
   
 #FileTime / NTFS / MFT Dec number
 try:
  ntfs = datetime(1601,1,1) + timedelta(microseconds=result/10)
  if ntfs > minDate and ntfs < maxDate:
   print("NTFS:", ntfs)
   final = ntfs
  else:
   print("NTFS outside of date range")
 except:
  print("Not valid NTFS time")
 #HFS Time
 try:
  hfs = datetime(1904,1,1) + timedelta(seconds=result)
  if hfs > minDate and hfs < maxDate:
   print("HFS+:", hfs)
   final = hfs
  else:
   print("HFS+ outside of date range")
 except:
  print("Not valid HFS+ time")
 #iOS Time
 try:
  ios = datetime.fromtimestamp(result+ 978325200)
  if ios > minDate and ios < maxDate:
   print("iOS:", ios)
   final = ios
  else:
   print("iOS outside of date range")
 except:
  print("Not valid iOS time")
 #Unix Time
 try:
  unix = datetime.fromtimestamp(result)
  if unix > minDate and unix < maxDate:
   print("Unix:", unix)
   final = unix
  else:
   print("Unix outside of date range")
 except:
  print("Not valid Unix time")
 #APFS Time
 try:
  apfs = datetime.fromtimestamp(result/1000)
  if apfs > minDate and apfs < maxDate:
   print("APFS:", apfs)
   final = apfs
  else:
   print("APFS outside of date range")
 except:
  print("Not valid APFS time") 
  
 return final
 
if ".csv" in argv[1]:
 #iterate through cells and try to convert stuff
 print("csv file")
 r = open(argv[1])
 csv_read = csv.reader(r)
 w = open("Timestamped " + argv[1], "w+")
 #csv_write = csv.writer(w)
 csv_write = csv.writer(w, lineterminator='\n')
 for row in csv_read:
  for i in range(len(row)):
   print(row[i])
   row[i] = timestamp(row[i])

  csv_write.writerow(row)
else:
 stampArg=argv[1]
 timestamp(stampArg)