inputfile = 'template_in.txt'
templatefile = 'template.txt'
outputfile = 'template_out.txt'

template = open(templatefile).read()

with open(inputfile) as file:
    with open(outputfile, 'w') as output:
        line = file.readline()
        while line:
            output_line = template.format(line[0:len(line)-1])
            output.write(output_line + '\n')
            line = file.readline()
        
