# document_api
 an intelligent document processing system that can extract, analyse, and summarise content from various document formats (PDF, DOCX, image with text). The system must leverage AI to understand document structure and extract key information automatically. 

# Data Extraction API

## Description
This API extracts, analyzes, and summarizes documents (PDF, DOCX, Images).
It uses OCR and NLP techniques to extract structured information.

## Tech Stack
Python (Flask)
 PyPDF2 (PDF parsing)
python-docx (DOCX parsing)
 Tesseract OCR (image text extraction)
 spaCy (entity extraction)
-TextBlob (sentiment analysis)
flask-cors

## Architecture Overview

The system follows a client-server architecture for intelligent document processing:

1.**Client Layer**
   -User uploads a document (PDF, DOCX, or image)
   -The file is converted into Base64 format
   -A POST request is sent to the API endpoint

2.**API Layer (Flask Backend)**
   -Receives the request with Base64-encoded file
   -Validates API key for authentication
   -Decodes Base64 into original file format

3.**Document Processing Layer**
   -PDF: Extract text using PyPDF2
   -DOCX: Extract text using python-docx
   -Image: Extract text using OCR (pytesseract)

4.**NLP Processing Layer**
   -Named Entity Recognition using spaCy
   -Sentiment Analysis using TextBlob
   -Text summarization using sentence extraction

5.**Response Layer**
   -Returns structured JSON response:
     -Summary
     -Extracted entities (names, dates, organizations, amounts)
     -Sentiment (Positive / Neutral / Negative)

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

## Known Limitations
-OCR may not work perfectly on low-quality images
-Large files may take more processing time
-Basic summarization (can be improved with advanced models)