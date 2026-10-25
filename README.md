# 📧 Spam Mail Detector

A machine learning project that classifies email / SMS messages as **Spam** or **Ham (not spam)**. The trained model runs directly in the browser, so the app can be hosted for free as a static website (for example on Netlify) with no backend or API.

🔗 **Live Demo:** https://guru-postmark.netlify.app/

---

## 📌 Overview

Spam messages waste time and can be used for phishing and scams. This project builds a text classifier that learns from thousands of labelled messages and predicts whether a new message is spam, along with a confidence score.

## ✨ Features

- Classifies any pasted email or SMS text as Spam or Ham
- Shows the spam and ham probability for each prediction
- Built-in example messages for quick testing
- Model performance section with accuracy and confusion matrix
- Runs fully in the browser (no server, no API calls)

## 🛠️ Tech Stack

| Part | Tools |
|------|-------|
| Language | Python, JavaScript |
| ML / Data | scikit-learn, pandas |
| Text features | TF-IDF (`TfidfVectorizer`) |
| Algorithm | Multinomial Naive Bayes |
| Frontend | HTML, CSS, JavaScript |
| Hosting | Netlify (static site) |
| Experimentation | Google Colab |

## 📊 Dataset

[SMS Spam Collection](https://github.com/justmarkham/pycon-2016-tutorial/blob/master/data/sms.tsv): about 5,570 labelled messages (`ham` or `spam`).

## ⚙️ How It Works

1. **Load data:** read the labelled SMS dataset with pandas and map `ham → 0`, `spam → 1`.
2. **Split:** 80% training and 20% testing (`random_state=42`).
3. **Feature extraction:** convert text to numbers with TF-IDF, removing English stop words. The vectorizer is fitted on training data only, to avoid data leakage.
4. **Train:** fit a Multinomial Naive Bayes classifier.
5. **Evaluate:** accuracy, confusion matrix, precision, recall and F1-score on the unseen test set.
6. **Export:** the vocabulary, IDF weights and Naive Bayes probabilities are saved to `model.json`.
7. **Predict in the browser:** JavaScript applies the same TF-IDF and Naive Bayes calculation to the user's message.

## 📈 Results

| Metric | Value |
|--------|-------|
| Accuracy | **97.85%** |
| Spam precision | 100% |
| Spam recall | 83.9% |
| Ham recall | 100% |

**Confusion matrix (test set of 1,115 messages)**

|  | Predicted Ham | Predicted Spam |
|--|:-:|:-:|
| **Actual Ham** | 966 | 0 |
| **Actual Spam** | 24 | 125 |

The model never marked a genuine message as spam, and it caught about 84% of the spam. The remaining 24 spam messages were missed.

## 📁 Project Structure

```
Spam-detection_Using_ML/
├── Spam Detection app/
│   ├── index.html                  # web app (UI + prediction logic)
│   ├── model.json                  # exported trained model
│   ├── train_export.py             # trains the model and creates model.json
│   ├── spam-detector-netlify.zip   # ready-to-upload bundle (netlify_site/ with index.html + model.json)
│   └── README.md                   # notes for this folder
├── spam_mail_detection.txt         # the full Colab / terminal script (Python saved as .txt)
├── requirementss.txt               # Python dependencies (pandas, scikit-learn)
└── README.md
```

`spam_mail_detection.txt` is the original experiment: it downloads the dataset, trains and evaluates the model, prints the accuracy, confusion matrix and classification report, and then classifies five sample messages. `train_export.py` does the same training and then writes `model.json` for the website. To run `spam_mail_detection.txt`, save a copy with a `.py` extension.

## 🚀 Run Locally

**Use the web app**

```bash
cd "Spam Detection app"
python -m http.server 8000
```

Then open `http://localhost:8000`. (A local server is needed because the page loads `model.json`.)

**Retrain the model**

```bash
pip install -r requirementss.txt
cd "Spam Detection app"
curl -o sms.tsv https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv
python train_export.py
```

`train_export.py` reads `sms.tsv` from the folder you run it in and overwrites `model.json` there, so the web app picks up the new model straight away. It prints the accuracy and confusion matrix when it finishes.

## 🌐 Deployment

The site is just `index.html` plus `model.json`, so any static host works. To use [Netlify](https://www.netlify.com/), unzip `Spam Detection app/spam-detector-netlify.zip` and drag the `netlify_site` folder onto Netlify. Deploying the whole `Spam Detection app` folder also works, but it would publish `train_export.py` and the zip as well.

## 🔮 Future Improvements

- Train on a larger email-specific dataset to handle long emails better
- Compare with other models (Logistic Regression, SVM, Random Forest)
- Improve spam recall with threshold tuning
- Add batch file upload for checking many messages at once

## 👤 Author

Guru Charan M
B.Tech CSE (AI), Saveetha University


## 📄 License

This project is for educational purposes.
