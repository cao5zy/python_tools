import re, sys


def isvalid_line(line):
    return re.match(r'^import.+from.+', line) != None

def parse_import(line):
    if not isvalid_line(line): return []
    
    removed_import = line.replace('import', '')
    #  print(removed_import)
    removed_from = re.sub('from.*', '', removed_import)
    #  print(removed_from)
    removed_bracket = removed_from.replace('{', '').replace('}', '')
    #  print(removed_bracket)
    items = list(map(lambda item:item.strip(), removed_bracket.split(',')))
    # print(items)
    return items

def parse_from(line):
    if not isvalid_line(line): return ''

    result = re.search(r'''from\s+['"]([\w_\-\./\@]+)['"]\s*;?''', line)
    return result.group(1) if result else ''

def gen_entry(name, items):
    fitems = ','.join(list(map(lambda item: f'''"{item}":{{}}''', items)))
    return f'''"{name}":{{{fitems}}}'''


def main():
    filePath = sys.argv[1]
    print('parse file:' + filePath)
    with open(filePath, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            if isvalid_line(line):
                print(gen_entry(
                    parse_from(line),
                    parse_import(line)) + ',')
            line = file.readline()
        
if __name__ == '__main__':
    main()
