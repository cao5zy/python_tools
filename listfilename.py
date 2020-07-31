import sys
import os

dir_path = sys.argv[1]

for root, dirs, files in os.walk(dir_path):
    for filename in files:
        print(filename)
