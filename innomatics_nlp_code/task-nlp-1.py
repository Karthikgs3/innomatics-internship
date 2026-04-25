import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

text = "This is a sample sentence for NLP preprocessing!!!"

text = text.lower()
text = re.sub(r'[^a-z\s]', '', text)

tokens = word_tokenize(text)

filtered = [word for word in tokens if word not in stopwords.words('english')]

print(filtered)