# Dataset

The original RAR archive contained a CSV with 5,457 URL records, 87 extracted URL-characteristic columns, a `url` field, and a `status` classification label. The CSV itself is not included in this GitHub upload.

Download the dataset from the source used for this project:

https://www.kaggle.com/datasets/jayaprakashpondy/hacking-breaches-dataset

Save the downloaded CSV in this folder as `upload.csv`.

The source notebook's actual training pipeline uses only `url` as the input text and `status` as the target. The 87 engineered feature columns are present in the CSV but are not used by that notebook's classifier.
