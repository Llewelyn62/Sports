# From https://automatetheboringstuff.com/chapter13/
import PyPDF2 as PDF
with open('/Users/Llewelyn_home/Downloads/Slow_slip.pdf', 'rb') as pdfFileObj: 
    pdfReader = PDF.PdfFileReader(pdfFileObj)
    print(pdfReader.getNumPages())
    page1 = pdfReader.getPage(0)
    print(page1.extractText())