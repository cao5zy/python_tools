import re


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

    result = re.search(r'''from\s+['"]([\w_-]+)['"]\s*;?''', line)
    return result.group(1) if result else ''

def gen_entry(name, items):
    fitems = ','.join(list(map(lambda item: f'''{{name:"{item}"}}''', items)))
    return f'''{{name:"{name}",includes:[{fitems}]}}'''
