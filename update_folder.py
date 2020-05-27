import os
import sys

def get_file_names(dirName):
    fileList = []
    for root, dirs, files in os.walk(dirName):
        if('.env' in root):continue
        if('.git' in root):continue
        for file in files:
            fileName = os.path.join(root,file)
            if '~' in fileName or '#' in fileName :continue
            fileList.append(fileName)
    return fileList


if __name__ == '__main__':
    print(sys.argv[1])
    print(get_file_names(sys.argv[1]))
