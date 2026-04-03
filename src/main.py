import base64, tempfile, os
from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
import docx
import pytesseract
from PIL import Image
import spacy
from textblob import TextBlob
import os

app = Flask(__name__)
API_KEY = "sk_track2_987654321"
nlp = spacy.load("en_core_web_sm")

# Text extraction from pdf

def extract_pdf(path):
    reader = PdfReader(path)
    return "".join([p.extract_text() or "" for p in reader.pages])

# Text extraction from document
def extract_docx(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

# Text extraction from images
def extract_image(path):
    try:
        return pytesseract.image_to_string(Image.open(path))
    except:
        return "OCR not supported"

# -------- NLP -------- #

def summary(text):
    return text[:300]

def entities(text):
    doc = nlp(text)
    data = {"names":[], "dates":[], "organizations":[], "amounts":[]}

    for ent in doc.ents:
        if ent.label_=="PERSON": data["names"].append(ent.text)
        if ent.label_=="DATE": data["dates"].append(ent.text)
        if ent.label_=="ORG": data["organizations"].append(ent.text)
        if ent.label_=="MONEY": data["amounts"].append(ent.text)

    return {k:list(set(v)) for k,v in data.items()}

def sentiment(text):
    p = TextBlob(text).sentiment.polarity
    return "Positive" if p>0 else "Negative" if p<0 else "Neutral"

# -------- API -------- #

@app.route("/api/document-analyze", methods=["POST"])
def analyze():
    try:
        if request.headers.get("x-api-key") != API_KEY:
            return jsonify({"error":"Unauthorized"}),401

        data = request.json
        file_bytes = base64.b64decode(data["fileBase64"])

        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(file_bytes)
            path = f.name

        t = data["fileType"]

        if t=="pdf": text = extract_pdf(path)
        elif t=="docx": text = extract_docx(path)
        else: text = extract_image(path)

        if not text.strip():
            return jsonify({"error":"No text extracted"}),400

        return jsonify({
            "status":"success",
            "fileName":data["fileName"],
            "summary": summary(text),
            "entities": entities(text),
            "sentiment": sentiment(text)
        })

    except Exception as e:
        return jsonify({"error":str(e)}),500

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)

from flask_cors import CORS
CORS(app)