from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("This internship is really good")

print(result)