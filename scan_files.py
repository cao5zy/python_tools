from sys import argv
from os.path import join
from os import walk

def get_file_names(dirName):
    fileList = []
    for root, dirs, files in walk(dirName):
        if('.env' in root):continue
        if('.git' in root):continue
        for file in files:
            if file.find('.js') != -1:
                fileName = join(root,file)
                if '~' in fileName or '#' in fileName :continue
                fileList.append(fileName)
    return fileList

def get_lines_of_file(file_name):
    try:
        
        with open(file_name, 'r') as fileobj:
            list = []
            line = fileobj.readline()
            while line:
                list.append(line.replace('\n', ''))
                line = fileobj.readline()

            return list
    except Exception as ex:
        print(ex)
        return []
        
def main():
    targets_file=argv[1]
    target_folder=argv[2]

    print('targets_file:%s' % targets_file)
    file_names = get_file_names(target_folder)
    targets = get_lines_of_file(targets_file)

    res = []
    for file_name in file_names:
        lines = get_lines_of_file(file_name)

        temp = []
        for target in targets:
            tresult = list(filter(lambda line: target in line, lines))
            if len(tresult) != 0:
                temp.append('%s:%s'%(file_name, target))

        if len(temp) == 0:
            msg = '%s:no targst' % file_name
            print(msg)
        else:
            print('%s: found' % file_name)
            res.extend(temp)


    print('---------------------------------')
    [print(item) for item in res]
    

if __name__ == '__main__':
    main()
