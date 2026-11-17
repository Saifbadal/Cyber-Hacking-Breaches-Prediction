# Cyber Hacking Breaches Prediction and Detection Using Machine Learning

Bachelor's capstone project exploring phishing-versus-legitimate URL classification using Python, TF-IDF text vectorization, and a Random Forest classifier.

## Dataset

The repository includes the original `dataset/upload.csv` file:

- 5,457 URL records
- 90 columns: `Id`, `url`, 87 engineered URL/page/domain features, and `status`
- 2,737 phishing records (50.16%)
- 2,720 legitimate records (49.84%)
- No blank cells or duplicate URL values were found in the uploaded CSV.

See [docs/FEATURE_GUIDE.md](docs/FEATURE_GUIDE.md) for an explanation of all 87 engineered columns.

## Project structure

- `app.py` — Flask application supplied with the project.
- `model/model_training.ipynb` — reproducible training notebook based on the supplied workflow.
- `dataset/upload.csv` — original labelled URL dataset.
- `dataset/README.md` — dataset notes.
- `test_data/test_data.csv` — small set of sample labelled URLs.
- `requirements.txt` — Python dependencies.
- `Accuracy.txt` — accuracy figures reported in the supplied project materials.
- `PROJECT_STATUS.md` — remaining files needed to run the web interface.

## How the current notebook trains the model

The notebook selects the raw `url` column as text input and `status` as the target label. It converts URLs to TF-IDF vectors, uses a 70/30 train/test split (random state 250), trains a `RandomForestClassifier` (random state 0), evaluates predictions, and saves the fitted vectorizer and classifier with pickle.

**Important:** Although the CSV stores 87 engineered features, the notebook currently selects only `url` and `status`. The Random Forest in this notebook therefore learns from TF-IDF URL text; it does not use all 87 engineered feature columns. See the feature guide and the notebook before describing the model in a presentation.

## Train the model

1. Install dependencies: `pip install -r requirements.txt`.
2. Open `model/model_training.ipynb` in Jupyter.
3. Run the cells from top to bottom. The notebook looks for `dataset/upload.csv` (or `upload.csv` in the project root).
4. The notebook exports `model.pkl` and `tfidf_vectorizer.pkl` to the project root.

## Flask application status

The supplied `app.py` expects `model.pkl`, `tfidf_vectorizer.pkl`, and a `templates/` directory with HTML files. The model artifacts and HTML templates were **not present** in the uploaded RAR archive. Run the training notebook to generate the two pickle files, and recover or rebuild the HTML templates before running the web interface. See `PROJECT_STATUS.md`.

## Reported results

The supplied `Accuracy.txt` reports 99% training accuracy and 91% testing accuracy. These are the figures stated in the original project materials; rerun the notebook to independently reproduce them.

## Disclaimer

This is an academic demonstration, not a production-grade phishing protection system. A model prediction is not proof that a website is safe or malicious.
