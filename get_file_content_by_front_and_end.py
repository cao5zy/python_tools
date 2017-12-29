import re
import sys

infile = sys.argv[3]
outfile = sys.argv[4] if len(sys.argv) == 5 else 'output.txt'
startTag = sys.argv[1]
endTag = sys.argv[2]
def main():
	front = ""
	end = ""
	def getPart(str):
		return str[str.find(startTag) + len(startTag) + 1: str.find(endTag)]

	with open(infile) as fileRead:
		with open(outfile , 'w') as fileOut:
			fileOut.write(getPart(fileRead.read()))

if __name__ == '__main__':
	main()
	#python convert_to_deployment.py "a" "b", "ft.aspx" "output.txt" # replace a with b in ft.aspx and output to output.txt
	