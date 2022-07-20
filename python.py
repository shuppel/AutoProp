import PyPDF2
filename= input("Enter file name:")
pdfFileObj = open(filename,'rb')
pdfReader = pyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages

pageObj = pdfReader.getpage(0)
pageObj.extractText()