import tkinter as tk
from tkinter import filedialog
from docx import Document
from openai_api_service import analyze_text
import pdfplumber
import spacy


nlp = spacy.load("en_core_web_sm")

def truncate_text(text, max_tokens):
    doc = nlp(text)
    truncated_tokens = doc[:max_tokens]
    return "".join(token.text_with_ws for token in truncated_tokens), len(doc)


def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    extracted_text = []

    for paragraph in doc.paragraphs:
        extracted_text.append(paragraph.text)

    return "\n".join(extracted_text)


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        extracted_text = []
        for page in pdf.pages:
            extracted_text.append(page.extract_text())
        return "\n".join(extracted_text)


def main():
    max_allowed_tokens = 3000
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Document files", "*.docx *.pdf")])

    if file_path:
        if file_path.lower().endswith(".docx"):
            text = extract_text_from_docx(file_path)
        elif file_path.lower().endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        else:
            print("Unsupported file type.")
            return None

        print("Original text:")
        print(text)
        truncated_text, original_token_count = truncate_text(text, max_allowed_tokens)
        print(f"Original token count: {original_token_count}")
        print(f"Truncated token count: {len(truncated_text.split())}")
        summary = analyze_text(truncated_text)
        print("Summary:")
        print(summary)
    else:
        print("No file selected.")
        return None



if __name__ == "__main__":
    main()

