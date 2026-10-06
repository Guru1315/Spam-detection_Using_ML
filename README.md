
📧 Spam Mail Detector

A machine learning project that classifies email / SMS messages as Spam or Ham (not spam). The trained model runs directly in the browser, so the app can be hosted for free as a static website (for example on Netlify) with no backend or API.

🔗 Live Demo: https://guru-postmark.netlify.app/

📌 Overview

Spam messages waste time and can be used for phishing and scams. This project builds a text classifier that learns from thousands of labelled messages and predicts whether a new message is spam, along with a confidence score.

✨ Features
Classifies any pasted email or SMS text as Spam or Ham
Shows the spam and ham probability for each prediction
Built-in example messages for quick testing
Model performance section with accuracy and confusion matrix
Runs fully in the browser (no server, no API calls)
🛠️ Tech Stack
Part	Tools
Language	Python, JavaScript
ML / Data	scikit-learn, pandas
Text features	TF-IDF (TfidfVectorizer)
Algorithm	Multinomial Naive Bayes
Frontend	HTML, CSS, JavaScript
Hosting	Netlify (static site)
Experimentation	Google Colab
📊 Dataset

SMS Spam Collection: about 5,570 labelled messages (ham or spam).

⚙️ How It Works
Load data: read the labelled SMS dataset with pandas and map ham → 0, spam → 1.
Split: 80% training and 20% testing (random_state=42).
Feature extraction: convert text to numbers with TF-IDF, removing English stop words. The vectorizer is fitted on training data only, to avoid data leakage.
Train: fit a Multinomial Naive Bayes classifier.
Evaluate: accuracy, confusion matrix, precision, recall and F1-score on the unseen test set.
Export: the vocabulary, IDF weights and Naive Bayes probabilities are saved to model.json.
Predict in the browser: JavaScript applies the same TF-IDF and Naive Bayes calculation to the user's message.
📈 Results
Metric	Value
Accuracy	97.85%
Spam precision	100%
Spam recall	83.9%
Ham recall	100%

Confusion matrix (test set of 1,115 messages)

	Predicted Ham	Predicted Spam
Actual Ham	966	0
Actual Spam	24	125

The model never marked a genuine message as spam, and it caught about 84% of the spam. The remaining 24 spam messages were missed.

📁 Project Structure
spam-detector/
├── netlify_site/
│   ├── index.html        # web app (UI + prediction logic)
│   └── model.json        # exported trained model
├── training/
│   └── train_export.py   # trains the model and creates model.json
└── README.md
🚀 Run Locally

Use the web app

bash
cd netlify_site
python -m http.server 8000

Then open http://localhost:8000. (A local server is needed because the page loads model.json.)

Retrain the model

bash
pip install pandas scikit-learn
cd training
# place sms.tsv (the dataset) in this folder
python train_export.py

Copy the new model.json into netlify_site/.

🌐 Deployment

The netlify_site folder is a static site. Drag and drop it onto Netlify, or connect this GitHub repo and set the publish directory to netlify_site.

🔮 Future Improvements
Train on a larger email-specific dataset to handle long emails better
Compare with other models (Logistic Regression, SVM, Random Forest)
Improve spam recall with threshold tuning
Add batch file upload for checking many messages at once
👤 Author

Guru Charan M B.Tech CSE (AI), Saveetha University 
