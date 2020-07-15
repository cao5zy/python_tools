import os
import sys
import shutil

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
    if not os.path.exists(filePath): return None
    
    st = os.stat(filePath)
    return st.st_mtime or st.st_ctime

def get_target_file_name(source_path, target_path):
    def compose_target_path(file_name):
        return os.path.join(target_path, file_name[len(source_path)+1:])

    return compose_target_path

def get_target_file_dir(target_file):
    return os.path.split(target_file)[0]

def get_copy_file(get_target_path):
    def copy_file(source_file):
        print(get_target_path(source_file))
        shutil.copy(source_file, get_target_path(source_file))
    return copy_file

def ensure_target_dir(get_target_path):
    def create_target_dir(source_file):
        target_dir = os.path.split(get_target_path(source_file))[0]
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

    return create_target_dir
if __name__ == '__main__':
    source_path = sys.argv[1]
    target_path = sys.argv[2]
    get_target_path = get_target_file_name(source_path, target_path)

    copy_file = get_copy_file(get_target_path)
    ensure_dir = ensure_target_dir(get_target_path)
    
    filter_files = lambda source, target: get_file_time(target) == None or get_file_time(source) > get_file_time(target)
    
    transferred_files = filter(lambda f:filter_files(f, get_target_path(f)), get_file_names(sys.argv[1]))

    for source_file in transferred_files:
        ensure_dir(source_file)
        print('copied:' + source_file)
        copy_file(source_file)
        
# 例子：python3 update_folder.py /Users/caozy/Documents/projects/python_tools /Users/caozy/Documents/projects/PH_Taro_1/cxy
# 不会拷贝python_tools文件夹，只会拷贝python_tools下的所有文件和文件夹到文件夹cxy中

