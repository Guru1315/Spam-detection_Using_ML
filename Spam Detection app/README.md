# Spam Detection app

The web app and the code that builds its model. The project overview, results and background are in the [main README](../README.md).

| File | What it is |
|---|---|
| `index.html` | The whole web app: page, styles and prediction logic in one file |
| `model.json` | The trained model, exported as JSON so the browser can use it |
| `train_export.py` | Trains the model on `sms.tsv` and writes `model.json` |
| `spam-detector-netlify.zip` | A bundle for Netlify containing a `netlify_site/` folder with `index.html` and `model.json` |

## What is inside `model.json`

| Key | Contents |
|---|---|
| `vocab` | Each known word and its column number (7,441 words) |
| `idf` | The TF-IDF weight for each word |
| `log_prob` | Naive Bayes log-probabilities of each word for ham and for spam |
| `log_prior` | Log-probability of each class before seeing a message |
| `accuracy`, `confusion` | Test-set results, shown under "Model performance" on the page |
| `train_size`, `test_size` | 4,457 training and 1,115 test messages |

## How the page predicts

1. It loads `model.json` with `fetch`, so it must be served over HTTP. Opening the file straight from disk will not work.
2. It splits the message into words the same way scikit-learn does (lower-cased, two or more letters, digits or underscores).
3. It applies the saved TF-IDF weights, adds up the Naive Bayes scores for ham and spam, and shows the spam and ham probabilities with a bar.

Nothing is sent anywhere. The prediction runs entirely in the browser.

## Run it

```bash
python -m http.server 8000
```

Open http://localhost:8000.

## Retrain

```bash
pip install -r ../requirementss.txt
curl -o sms.tsv https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv
python train_export.py
```

`sms.tsv` is not stored in the repository, so download it first. Retraining overwrites `model.json`. The zip is not updated automatically, so rebuild it if you want the Netlify bundle to match.
