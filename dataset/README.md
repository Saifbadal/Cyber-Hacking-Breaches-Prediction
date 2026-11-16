# Dataset

The original project CSV contains 5,457 URL records, 87 extracted URL-characteristic columns, the URL column, and the classification label. It is included as `upload.csv.gz` in this folder to reduce repository size.

To extract it, use:

```bash
gzip -dk dataset/upload.csv.gz
```

This creates `dataset/upload.csv`. The notebook can also read the compressed `.csv.gz` directly.

The training notebook follows the source project's actual pipeline: it selects the `url` column and `status` label, then applies TF-IDF. Although the dataset contains 87 engineered feature columns, those columns are not used by the supplied notebook's classifier.
