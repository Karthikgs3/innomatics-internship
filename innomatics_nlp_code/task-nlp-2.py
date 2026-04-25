from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = ["I love this product", "This is bad", "Amazing experience", "Worst service"]
labels = [1, 0, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

test = ["I love this"]
test_vec = vectorizer.transform(test)

print(model.predict(test_vec))