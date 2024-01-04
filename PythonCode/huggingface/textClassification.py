from transformers import pipeline, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

text = "This movie is really good!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

print(f"Input text: {text}")
print(f"Predicted label: {outputs[0]['label']}, score: {outputs[0]['score']:.2f}")