# This Python file uses the following encoding: utf-8

from pyPdf import PdfFileWriter, PdfFileReader
import sys
import os

filelist = os.listdir(".")

filelist.sort() # 파일 오름차순으로 정렬

num = len(filelist)
output = PdfFileWriter()

for filename in filelist :
	
	input = PdfFileReader(file(filename,"rb"))
	for j in range(input.getNumPages()):
		output.addPage(input.getPage(j))

outputStream = file("final.pdf","wb")
output.write(outputStream)
outputStream.close()