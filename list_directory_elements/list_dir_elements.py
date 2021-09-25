import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', "--dir", help="Target Directory", type=str, default="./")
parser.add_argument('-e', "--extension", help="Filter to display files of only a specific extension", type=str, default="")
args = parser.parse_args()

path = args.dir
ext = args.extension

print("Arguments--> Directory: ",path," Extension: ",ext,"\n")

dir_list =  os.listdir(path);

for i in dir_list:
    if i.endswith(ext):
        print(i);

