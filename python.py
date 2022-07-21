# extract_doc_info.py
from PyPDF2 import PdfFileReader
pdf_path = "testfile.pdf"

page=0

def extract_information(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf = PdfFileReader(f)
        print(pdf.numPages)
        currentpage = pdf.getPage(page)
        pdfData=currentpage.extractText()
        print(pdfData)

for x in page:
    print(pdfData)
    page + 1

path = pdf_path
extract_information(path)


