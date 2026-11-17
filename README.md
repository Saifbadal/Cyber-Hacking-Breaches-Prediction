# Cyber Hacking Breaches Prediction and Detection Using Machine Learning

Bachelor's capstone project for identifying phishing and legitimate website URLs using Python, TF-IDF text vectorization, and a Random Forest classifier.

## Repository structure

The original application and its supporting files are organized inside the **`SOURCE CODE/`** folder.

```text
Cyber-Hacking-Breaches-Prediction/
│
├── README.md
├── Accuracy.txt
├── .gitignore
├── dataset/
│   └── upload.csv
│
└── SOURCE CODE/
    ├── app.py
    ├── model.pkl
    ├── tfidf_vectorizer.pkl
    ├── Accuracy.txt
    ├── requirements.txt
    ├── upload.csv
    ├── model/
    │   ├── model.ipynb
    │   ├── model.pkl
    │   ├── tfidf_vectorizer.pkl
    │   └── Dataset/
    │       └── upload.csv
    ├── templates/
    │   ├── index.html
    │   ├── performance.html
    │   ├── chart.html
    │   ├── login.html
    │   ├── upload.html
    │   ├── preview.html
    │   └── prediction.html
    ├── static/
    │   ├── css/
    │   ├── js/
    │   ├── img/
    │   ├── fonts/
    │   └── webfonts/
    └── test_data/
        └── test_data.csv
```

The `static/` folder contains the web application's stylesheets, JavaScript, images, and fonts. The `templates/` folder contains the HTML pages rendered by Flask.

## Dataset

The repository includes `dataset/upload.csv` (also copied in the original `SOURCE CODE/` folders).

- **5,457 URL records**
- **90 columns:** `Id`, `url`, 87 URL/page/domain characteristics, and `status`
- **2,737 phishing** records (50.16%)
- **2,720 legitimate** records (49.84%)

The `status` column is the target label: `phishing` or `legitimate`. The 87 other columns describe URL structure, page/HTML behaviour, and domain/reputation signals.

## Technologies

- Python 3.10.9
- Flask — web application
- Pandas and NumPy — data handling
- Scikit-learn — TF-IDF vectorization, train/test split, Random Forest, and model evaluation
- Pickle — saving and loading the trained model and vectorizer
- HTML, CSS, and JavaScript — web interface

## How the project works

1. A URL is entered through the Flask web interface.
2. The input URL is passed to the TF-IDF vectorizer.
3. The vectorizer transforms the URL text into a numeric feature vector using the vocabulary learned during training.
4. The saved Random Forest model receives that vector and predicts a class.
5. The Flask application displays the result as `phishing` or `legitimate`.

**Important implementation detail:** The supplied notebook uses the raw `url` column as its input (`X = data['url']`) and `status` as its label (`y = data['status']`). It trains on TF-IDF text vectors. Although the uploaded `upload.csv` contains 87 engineered URL/page/domain feature columns, the notebook does **not** pass those 87 columns into the Random Forest model.

## Run the existing Flask application

The trained model and vectorizer, templates, and static assets are already inside `SOURCE CODE/`. Run the application from that folder so its relative file paths resolve correctly.

1. Install Python 3.10.9 (or a compatible Python version).
2. Open a terminal in the repository folder.
3. Change directory to the source folder:

   ```bash
   cd "SOURCE CODE"
   ```

4. Install the dependencies listed in `requirements.txt`. The supplied file contains `pip install` command lines, so you can run the commands in that file individually, or use:

   ```bash
   python -m pip install Flask==2.3.2 scikit-learn==1.2.2 pandas==2.0.0 numpy==1.23.5 matplotlib==3.7.1 pymsgbox==1.0.9
   ```

5. Start Flask:

   ```bash
   python app.py
   ```

6. Open the local address shown in the terminal, normally `http://127.0.0.1:5000/`.

The application loads `model.pkl` and `tfidf_vectorizer.pkl` from the `SOURCE CODE/` folder and renders pages from `SOURCE CODE/templates/`.

## About the training notebook

Open `SOURCE CODE/model/model.ipynb` in Jupyter Notebook or JupyterLab.

The saved notebook outputs document a dataset of **11,430 rows and 89 columns**, with 5,715 legitimate and 5,715 phishing records. The code in the notebook loads a file named `dataset_phishing.csv`; that exact filename is not present in the repository tree. The repository's `upload.csv` is a separate 5,457-row, 90-column dataset, so it should not be substituted into the notebook without updating the data-loading and validation steps.

The notebook's recorded run shows:
- Training accuracy: **0.99975** (about 99.98%)
- Testing accuracy: **0.91659** (about 91.66%)
- Test set size: **3,429**
- Classification report and confusion matrix are included in the notebook outputs.

The project's `Accuracy.txt` reports the rounded figures as 99% training accuracy and 91% testing accuracy.

## Notes and limitations

- Use the saved `model.pkl` and `tfidf_vectorizer.pkl` for the supplied Flask demo.
- To reproduce model training exactly, obtain the original `dataset_phishing.csv` file used by the notebook, or deliberately update the notebook to use the included `upload.csv` and then retrain and re-evaluate.
- The notebook's saved training outputs are historical results; rerun the code to verify results in your own environment.
- This is an academic demonstration, not a production-grade phishing protection system. A prediction is not proof that a website is safe or malicious.
