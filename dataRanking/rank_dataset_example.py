import sys
import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
import pandas, random
import nltk
from dataIngestion.dataset_clean import cleaning
from dataRanking.rank_dataset import rank_dataset

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("query required")
        exit()

    # Clean the data
    print("Cleaning data...")
    p = 0.02
    review = pandas.read_csv('../dataIngestion/dataset.csv', skiprows=lambda i: i > 0 and random.random() > p)
    review.review_text = review.review_text.astype('str')
    nltk.download('stopwords')
    cleaning(review, 'review_text')

    # Get the query
    query = sys.argv[1].lower()

    # Rank the dataset
    print("Ranking....")
    result = rank_dataset(review, query)
    print("Top 10 ranked reviews + title")
    print(result.head(10))