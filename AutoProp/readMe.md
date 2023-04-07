To set up the environment and install the necessary library, follow these steps:

1: Create a new Python project and set up a virtual environment.

2: Install the python-docx library with the following command:

pip install python-docx

Create a new file called proposal_ingestion_service.py and add the above code to the file.

Replace "path/to/your/word/document.docx" with the path to the actual Word document you want to process.

Run the code with the following command:


python proposal_ingestion_service.py
# Proposal Ingestion Service

This Python script extracts text from a Microsoft Word document using the `python-docx` library. The main function in the script processes a given Word document and prints the extracted text.

## Setup

1. Ensure that Python 3.x is installed on your system.

2. Set up a virtual environment and activate it:

python -m venv venv
source venv/bin/activate (Linux/macOS)
venv\Scripts\activate (Windows)

3. Install the required libraries:
pip install python-docx


## Usage

1. Edit the `proposal_ingestion_service.py` file and replace the `docx_path` variable with the path to your Word document.

2. Run the script:
python proposal_ingestion_service.py


3. The extracted text will be printed in the console.

## Customization

You can customize the `extract_text_from_docx` function to process the Word document differently, such as extracting text from tables or processing specific sections of the document.
