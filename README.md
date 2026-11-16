# Cyber Hacking Breaches Prediction and Detection Using Machine Learning

Bachelor's capstone project exploring phishing-versus-legitimate URL classification using Python, TF-IDF text vectorization, and a Random Forest classifier.

## Project structure

- `app.py` — Flask application supplied with the project.
- `model/model_training.ipynb` — reproducible training notebook based on the supplied notebook workflow.
- `dataset/upload.csv.gz` — compressed original dataset (5,457 rows; includes 87 engineered URL-characteristic columns).
- `dataset/README.md` — dataset details and extraction instructions.
- `test_data/test_data.csv` — sample labelled URLs.
- `requirements.txt` — Python dependencies.
- `Accuracy.txt` — accuracy figures reported in the supplied project materials.
- `PROJECT_STATUS.md` — files missing from the uploaded archive and steps needed to run the web interface.

## How the model works

The supplied training workflow selects the `url` text column and the `status` label. It converts URLs into TF-IDF vectors, uses a 70/30 train/test split (random state 250), trains a `RandomForestClassifier` (random state 0), evaluates predictions, and saves the fitted vectorizer and classifier with pickle.

**Important dataset distinction:** The CSV has 87 URL-characteristic columns in addition to the URL and label. The notebook's actual training code selects only the raw `url` column and applies TF-IDF; it does not feed all 87 engineered columns into the classifier.

## Train the model

1. Install dependencies: `pip install -r requirements.txt`.
2. Open `model/model_training.ipynb` in Jupyter.
3. Run the cells from top to bottom. The notebook looks for `dataset/upload.csv.gz` or an extracted `upload.csv`.
4. The notebook exports `model.pkl` and `tfidf_vectorizer.pkl` to the working directory.

## Flask application status

The supplied `app.py` expects `model.pkl`, `tfidf_vectorizer.pkl`, and a `templates/` directory with HTML files. Those trained artifacts and HTML templates were **not present** in the uploaded archive, so the web interface is not yet runnable from this repository as committed. See `PROJECT_STATUS.md`.

## Reported results

The supplied `Accuracy.txt` reports 99% training accuracy and 91% test accuracy. These are the figures stated in the original project materials; rerun the notebook to independently reproduce them.

## Disclaimer

This is an academic demonstration, not a production-grade phishing protection system. A model prediction is not proof that a website is safe or malicious.
