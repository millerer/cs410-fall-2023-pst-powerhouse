import pandas as pd
from FlairSentimentAnalysis.flair_predict import predict
from concurrent.futures import ThreadPoolExecutor
import argparse
import sys

sys.path.append('../')
from dataIngestion.dataset_clean import remove_EAR

def parallel_predict(text):
    return predict(text)

def calculate_avg_sentiment(group):
    return round(group['sentiment_score'].mean(), 3)

def clean_game_reviews(df):
    df['review_text'].fillna('', inplace=True)
    df['review_text'] = df['review_text'].apply(remove_EAR) # Remove Early Access Review
    df = df[df['review_text'].str.strip() != '']  # Remove all rows with empty review_text

    return df

def sample_reviews(group, N):
    if len(group) > N:
        return group.sample(N)
    else:
        return group

def main(game_titles, input_file, num_threads, sample_size):
    df = pd.read_csv(input_file)

    # Filter dataframe to include only the specified game titles
    df = df[df['app_name'].isin(game_titles)]

    # Clean game review texts
    df = clean_game_reviews(df)

    # Group by 'app_name' and apply the sampling function
    sampled_df = df.groupby('app_name', group_keys=False).apply(lambda group: sample_reviews(group, sample_size))

    # Calculate sentiment scores using the predict() function
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
         sampled_df['sentiment_score'] = list(executor.map(parallel_predict, sampled_df['review_text']))

    # Calculate average sentiment scores for each game title
    df_avg_sentiment = sampled_df.groupby('app_name').apply(calculate_avg_sentiment).reset_index()
    df_avg_sentiment.columns = ['app_name', 'avg_sentiment']

    # print(df_avg_sentiment)
    return df_avg_sentiment

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Calculates sentiment score for each review of a game and calculates average score')
    parser.add_argument('--titles', dest='game_titles', type=str, help='Comma separated list of games titles, eg: game1,game2...')
    parser.add_argument('--input', dest='input_file', type=str, help='Input file containing game reviews')
    parser.add_argument('-threads', dest='num_threads', type=int, default=4, help='Number of threads')
    parser.add_argument('-sample', dest='sample_size', type=int, default=10, help='Number of reviews per game to calculate sentiments')
    args = parser.parse_args()

    game_titles = args.game_titles.split(',')
    main(game_titles, args.input_file, args.num_threads, args.sample_size)
