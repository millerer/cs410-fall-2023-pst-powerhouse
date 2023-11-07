# Dataset Ingestion and Cleaning 
## Prerequisite
* Download dataset from https://www.kaggle.com/datasets/andrewmvd/steam-reviews/data  and save it under the folder dataIngestion/
* Run in python3.9+  (Tested on MacBook)

## Please install required packages by pip3
* !pip3 install pandas matplotlib wordcloud wget nltk

## cleaning(df, review_column)
The function "cleaning(df, review_column)" in dataset_clean.py is what you want to call for data cleaning.
Check example in dataset_clean_example_main.py

## Where is the dataset from?
`dataset.csv` is a big dataset file (over 2GB). This has been already downloaded from [Steam Review](https://www.kaggle.com/datasets/andrewmvd/steam-reviews/data)
It takes time to git clone. Maybe we should remove it from the git repo when you can manually download it from Kaggle.

## Why Steam Review dataset?
* Usability 10.0
* Size > 100MB - large enough
* Clean dataset - English words only
* Dataset size is big enough with 6.4 million reviews
