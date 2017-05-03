from pyPdf import PdfFileWriter, PdfFileReader
import sys

if len(sys.argv) is 1:
	print "Insert pdf name & number"
	exit()

if len(sys.argv) is 2:
	print "Insert number of pdf document"
	exit()

init_name = sys.argv[1]
num = int(sys.argv[2])

output = PdfFileWriter()

for i in range(num) :
	
	input = PdfFileReader(file(init_name,"rb"))
	for j in range(input.getNumPages()):
		output.addPage(input.getPage(j))
	print ("read file "+init_name+" complete ")
	init_name = init_name.replace(str(i+1),str(i+2))

outputStream = file("final.pdf","wb")
output.write(outputStream)
outputStream.close()