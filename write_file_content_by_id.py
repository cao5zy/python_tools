import re
import sys

infile = sys.argv[2]
templatefile = sys.argv[3]
outfile = sys.argv[4] if len(sys.argv) == 5 else 'output.txt'
idtag = sys.argv[1]
def main():
	def getPart(inputContent, templateContent):
		return templateContent.replace(idtag, inputContent)

	with open(infile, encoding='utf-8') as fileRead, open(templatefile, encoding='utf-8') as filetemplate, open(outfile , 'w', encoding='utf-8') as fileOut:
		fileOut.write(getPart(fileRead.read(), filetemplate.read()))

if __name__ == '__main__':
	main()
	#python convert_to_deployment.py "a" "b", "ft.aspx" "output.txt" # replace a with b in ft.aspx and output to output.txt
	