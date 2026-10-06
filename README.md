Live Deployment: https://guru-postmark.netlify.app/

📧 Spam Mail Detection using Machine Learning

A machine learning project that classifies SMS/email messages as Spam or Ham (Not Spam) using the Multinomial Naive Bayes algorithm and TF-IDF feature extraction.

📌 Overview

This project builds a text classification model that automatically detects spam messages. It uses a labeled SMS dataset, converts text into numerical features using TF-IDF vectorization, and trains a Naive Bayes classifier to distinguish between spam and legitimate (ham) messages.

🧠 How It Works
Data Loading – Downloads the SMS dataset (sms.tsv) directly from a public GitHub source.
Preprocessing – Maps labels (ham → 0, spam → 1) and splits data into training (80%) and testing (20%) sets.
Feature Extraction – Converts raw text messages into numerical vectors using TfidfVectorizer (with English stop-word removal).
Model Training – Trains a MultinomialNB (Naive Bayes) classifier on the TF-IDF features.
Evaluation – Reports accuracy, confusion matrix, and a full classification report (precision, recall, F1-score).
Custom Predictions – Tests the trained model on custom sample messages to demonstrate real-world predictions.
📂 Dataset

The dataset used is the SMS Spam Collection, a tab-separated file containing SMS messages labeled as ham or spam. It is downloaded automatically when the script runs — no manual download needed.

🛠️ Tech Stack
Python 3
pandas – data handling
scikit-learn – TF-IDF vectorization, Naive Bayes model, evaluation metrics
urllib – dataset download
📁 Project Structure
spam-mail-detection/
├── README.md
├── requirements.txt
└── spam_mail_detection.py

⚙️ Installation & Usage
Clone the repository:
   git clone https://github.com/<Guru1315>/spam-detection.git
   cd spam-detection
   
Install dependencies:
   pip install -r requirements.txt
   
Run the script:
   python spam_mail_detection.py

The script will automatically download the dataset, train the model, print evaluation metrics, and show predictions on sample custom messages.

📊 Sample Output
=== Model Accuracy: 96.77% ===

=== Confusion Matrix ===
True Negative (Ham correctly identified): 965
False Positive (Ham incorrectly marked as Spam): 0
False Negative (Spam incorrectly marked as Ham): 36
True Positive (Spam correctly identified): 114

=== Detailed Classification Report ===
              precision    recall  f1-score   support

         Ham       0.96      1.00      0.98       965
        Spam       1.00      0.76      0.86       150

(Actual numbers may vary slightly depending on train/test split.)

🔮 Future Improvements
Try other algorithms (Logistic Regression, SVM, Random Forest) for comparison
Use word embeddings (Word2Vec, GloVe) instead of TF-IDF
Deploy as a simple web app (Flask/Streamlit) for live message testing
Add support for email (not just SMS) datasets

📄 License :

This project is open-source and available under the MIT License.

🙋‍♂️ Author:

Built as part of academic coursework in Machine Learning / AI.
