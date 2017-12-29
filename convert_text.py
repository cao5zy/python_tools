import re
import sys

infile = sys.argv[3]
outfile = sys.argv[4] if len(sys.argv) == 5 else 'output.txt'
def main():

	with open(infile) as fileRead:
		with open(outfile , 'w') as fileOut:
			fileOut.write(re.sub(sys.argv[1], sys.argv[2], fileRead.read(), 0))

if __name__ == '__main__':
	main()
	#python convert_to_deployment.py "a" "b", "ft.aspx" "output.txt" # replace a with b in ft.aspx and output to output.txt
	