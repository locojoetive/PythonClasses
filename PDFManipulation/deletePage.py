from PyPDF2 import PdfFileWriter, PdfFileReader
infile = PdfFileReader('source.pdf', 'rb')
output = PdfFileWriter()

for i in xrange(infile.getNumPages()):
    p = infile.getPage(i)
    if p.getContents(): # getContents is None if  page is blank
        output.addPage(p)

with open('newfile.pdf', 'wb') as f:
   output.write(f)