# Project package status

The uploaded RAR archive included the Flask source file and model-training notebook, but did **not** include the following files that the Flask app expects:

- `model.pkl`
- `tfidf_vectorizer.pkl`
- `templates/index.html`
- `templates/performance.html`
- `templates/chart.html`
- `templates/login.html`
- `templates/upload.html`
- `templates/preview.html`
- `templates/prediction.html`

The training notebook exports the two pickle files after successful training. The HTML templates must be recovered from the original web-project folder or rebuilt before the Flask web interface can run. The full CSV dataset is included under `dataset/upload.csv.gz`; extract it or use the updated notebook, which can read the compressed file directly.
