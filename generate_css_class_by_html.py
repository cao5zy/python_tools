#! /bin/python
import re
import fluentpy as _

def get_class_name(lines):
    _(re.findall(r".*className='([\w\-]+)'.*", lines))\
    .filter(_.each != None) \
    .map(lambda n:'.'+n+' { }') \
    .map(print)


target_file = './generate_css.txt'

with open(target_file) as f:
    print(get_class_name(f.read()))

    
