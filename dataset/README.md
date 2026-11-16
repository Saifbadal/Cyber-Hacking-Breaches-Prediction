# Dataset

The uploaded project archive contains a 5,457-row URL dataset named `upload.csv` (about 1.67 MB). It was not uploaded in this commit, so download the source dataset from:

https://www.kaggle.com/datasets/jayaprakashpondy/hacking-breaches-dataset

Place the downloaded CSV in the repository root and name it `upload.csv`.

The CSV contains URL text, a label column (`status`), and URL-characteristic columns. In the supplied training notebook, the model uses the `url` column as text and the `status` column as the target; it does not currently use the 87 engineered feature columns.
