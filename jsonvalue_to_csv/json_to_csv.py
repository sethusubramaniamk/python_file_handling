import json
import os
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-d', "--dir", help="Target Directory", type=str, default="./")
parser.add_argument('-s', "--save", help="Filename (Example: sample.csv)  to save the data obtained from json file into csv, when left empty the script will just print the data and not save", type=str, default="")
parser.add_argument('-k', "--key", help="Key name to extract from a JSON file", type=str, default="")
args = parser.parse_args()

path = args.dir
filename = args.save
key = args.key
header = ["S.No","Value"]

print("Arguments--> Directory: ",path," Filename: ",filename," Key: ",key,"\n")

if(filename):
    f1 = open(filename, 'w', encoding='UTF8', newline='')
    writer = csv.writer(f1)
    # write the header
    writer.writerow(header)

dir_list =  sorted(os.listdir(path))
count=0
for i in dir_list:
    if i.endswith(".json"):
        f2 = open(path+i,'r')
        d = json.loads(f2.read())
        try:
            data = None
            if(d[key]):
                count+=1
                data = [count,d[key]]
                # write the data
                print(data)
                if(filename):
                    writer.writerow(data)
        except:
            pass
        f2.close()
if(filename):
    f1.close()
