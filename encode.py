import base64

with open("text.pdf", "rb") as f:
    encoded = base64.b64encode(f.read()).decode("utf-8")

with open("output.txt", "w") as f:
    f.write(encoded)

print("Saved to output.txt")