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


def get_file_time(filePath):
    st = os.stat(filePath)
    return st.st_mtime or st.st_ctime

def get_target_file_name(source_path, target_path):
    def compose_target_path(file_name):
        return os.path.join(target_path, file_name[len(source_path)+1:])

    return compose_target_path

if __name__ == '__main__':
    source_path = sys.argv[1]
    target_path = sys.argv[2]
    get_target_path = get_target_file_name(source_path, target_path)
    
#    list(map(lambda f:print(get_file_time(f)), get_file_names(sys.argv[1])))
    list(map(lambda f:print(get_target_path(f)), get_file_names(sys.argv[1])))    
