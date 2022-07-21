# extract_doc_info.py
from PyPDF2 import PdfFileReader
pdf_path = "testfile.pdf"


with open(pdf_path, "rb") as f:
    page = 0
    pdf = PdfFileReader(f)
    print("This document contains" + str(pdf.numPages))
    while page < pdf.numPages:
        currentpage=pdf.getPage(page)
        pdfData=currentpage.extractText()
        print(pdfData)
        page = page + 1







