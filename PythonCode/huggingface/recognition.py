from transformers import pipeline, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
model = pipeline("ner", model="dslim/bert-base-NER")

text = "Hugging Face is a startup based in New York City"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

for entity in outputs:
    print(f"Entity: {entity['word']}, Type: {entity['entity']}, Score: {entity['score']:.2f}")