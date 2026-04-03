# document_api
 an intelligent document processing system that can extract, analyse, and summarise content from various document formats (PDF, DOCX, image with text). The system must leverage AI to understand document structure and extract key information automatically. 

# Data Extraction API

## Description
This API extracts, analyzes, and summarizes documents (PDF, DOCX, Images).
It uses OCR and NLP techniques to extract structured information.

## Tech Stack
Python (Flask)
 PyPDF2 (PDF parsing)
-python-docx (DOCX parsing)
 Tesseract OCR (image text extraction)
 spaCy (entity extraction)
-TextBlob (sentiment analysis)

## Setup Instructions

 1.Clone repository
 2.Install dependencies:
   pip install -r requirements.txt

 3.Install spaCy model:
   python -m spacy download en_core_web_sm

4.Run:
   python src/main.py

## API Endpoint

POST /api/document-analyze

Headers:
x-api-key: sk_track2_987654321

## Approach

-Extract text from documents using format-specific libraries
-Use spaCy for Named Entity Recognition
-Use TextBlob for sentiment classification
-Generate summary using truncation for efficiency

## AI Tools Used
ChatGPT – used for guidance, debugging, and understanding concepts
spaCy – for entity extraction
TextBlob – for sentiment analysis