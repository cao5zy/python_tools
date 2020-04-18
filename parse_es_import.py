import re

def parse_import(line):
    removed_import = line.replace('import', '')
    #  print(removed_import)
    removed_from = re.sub('from.*', '', removed_import)
    #  print(removed_from)
    removed_bracket = removed_from.replace('{', '').replace('}', '')
    #  print(removed_bracket)
    items = list(map(lambda item:item.strip(), removed_bracket.split(',')))
    # print(items)
    return items
