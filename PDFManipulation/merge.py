from PyPDF2 import PdfFileMerger, PdfFileReader
import os


merger = PdfFileMerger()
files = [x for x in os.listdir() if x.endswith('.pdf')]

print(files)
for fname in sorted(files):
    merger.append(PdfFileReader(open(os.path.join('', fname), 'rb')))

merger.write("output.pdf")