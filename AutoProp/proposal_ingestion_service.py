from docx import Document

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    extracted_text = []

    for paragraph in doc.paragraphs:
        extracted_text.append(paragraph.text)

    return "\n".join(extracted_text)

def main():
    print("Welcome to the Word Document Text Extractor!")
    docx_path = input("Please enter the path to your Word document: ")
    
    try:
        text = extract_text_from_docx(docx_path)
        print("\nExtracted text from the document:\n")
        print(text)
    except Exception as e:
        print("Error: Unable to extract text from the document. Please check the file path and try again.")
        print(f"Details: {e}")

if __name__ == "__main__":
    main()
