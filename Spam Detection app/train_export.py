"""Train the model (same as the Colab notebook) and export it to model.json
so the website can run it in the browser. No server / API needed."""
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("sms.tsv", sep="\t", header=None, names=["label", "message"])
df["label_num"] = df.label.map({"ham": 0, "spam": 1})

X_train, X_test, y_train, y_test = train_test_split(
    df["message"], df["label_num"], test_size=0.2, random_state=42)

vec = TfidfVectorizer(stop_words="english")
Xtr = vec.fit_transform(X_train)
Xte = vec.transform(X_test)

model = MultinomialNB().fit(Xtr, y_train)
pred = model.predict(Xte)
acc = accuracy_score(y_test, pred)
cm = confusion_matrix(y_test, pred).tolist()
print("Accuracy:", acc, cm)

vocab = {w: int(i) for w, i in vec.vocabulary_.items()}
out = {
    "vocab": vocab,
    "idf": [round(float(x), 6) for x in vec.idf_],
    "log_prob": [[round(float(x), 6) for x in row] for row in model.feature_log_prob_],
    "log_prior": [float(x) for x in model.class_log_prior_],
    "accuracy": float(acc),
    "confusion": cm,
    "train_size": int(len(X_train)),
    "test_size": int(len(X_test)),
}
with open("model.json", "w") as f:
    json.dump(out, f, separators=(",", ":"))
