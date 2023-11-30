import pandas as pd
from flair_predict import predict
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
        return group.sample(N, random_state=1)  # Use a fixed random state for reproducibility
    else:
        return group

def main(input_file, output_file, num_threads, N):
    df = pd.read_csv(input_file)
    
    # Clean game review texts
    df = clean_game_reviews(df)

    # Group by 'app_name' and apply the sampling function
    sampled_df = df.groupby('app_name', group_keys=False).apply(lambda group: sample_reviews(group, N))

    # Calculate sentiment scores using the predict() function
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
         sampled_df['sentiment_score'] = list(executor.map(parallel_predict, sampled_df['review_text']))

    # Calculate average sentiment scores for each game title
    df_avg_sentiment = sampled_df.groupby('app_name').apply(calculate_avg_sentiment).reset_index()
    df_avg_sentiment.columns = ['app_name', 'avg_sentiment']

    # Save the sampled DataFrame to the output CSV file
    df_avg_sentiment.to_csv(output_file, index=False)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Produces an output .csv file containg average sentiment per game using N randomly sampled reviews')
    parser.add_argument('--input', dest='input_file', type=str, help='Input dataset')
    parser.add_argument('--output', dest='output_file', type=str, help='Output file path')
    parser.add_argument('-threads', dest='num_threads', type=int, default=4, help='Number of threads')
    parser.add_argument('-N', dest='N', type=int, default=100, help='Number of reviews per game to sample')
    args = parser.parse_args()

    main(args.input_file, args.output_file, args.num_threads, args.N)

