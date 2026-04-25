import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "This is a simple NLP task"

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

print(tags)