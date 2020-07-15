in_file = 'split_line.txt'
out_file = 'split_line_out.txt'


with open(in_file) as f:
    result = f.read()
    with open(out_file, 'w') as f1:
        for line in result.split('''\\n'''):
            print(line)
            f1.write(line + '\n')
        
        
