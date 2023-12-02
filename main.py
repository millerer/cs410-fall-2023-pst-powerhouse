import sys
import os
import pandas as pd, random
import nltk
import csv

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

import FlairSentimentAnalysis.predict_game_reviews_sentiments as predict_sentiment
from dataIngestion.dataset_clean import cleaning
from dataRanking.rank_dataset import rank_dataset


def write_csv(file_name, data):
    """ write a dataframe to a csv file """
    data.to_csv(file_name, index=False)

if __name__ == '__main__':
    # Expects a command line argument for the query. Use quotes if the query contians whitespace/more than one word
    if len(sys.argv) < 2:
        print('query required')
        exit()

    # Get the query
    query = sys.argv[1].lower()
    print('Received Query "%s"' %(query))

    # Get the data
    print('Getting data set...')
    p = 0.02
    review = pd.read_csv('dataIngestion/dataset.csv', skiprows=lambda i: i > 0 and random.random() > p)
    review.review_text = review.review_text.astype('str')

    # Clean the data
    print('Cleaning data...')
    nltk.download('stopwords')
    cleaning(review, 'review_text')

    # Rank the dataset
    print('Ranking....')
    result = rank_dataset(review, query, 20)

    # Get sentiment analysis for the game titles
    print('Calculating sentiment...')
    sentiment = predict_sentiment.main(result['app_name'],'dataIngestion/dataset.csv', 5, 10)

    # Merge the rank and sentiment data, write to csv file
    print('Writing results...')
    result = pd.merge(result, sentiment[['avg_sentiment','app_name']], on='app_name')
    result = result.sort_values(by='rank', ascending=False)
    # print(result)
    write_csv('summary.csv', result)