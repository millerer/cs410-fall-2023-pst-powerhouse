import pandas as pd
from flair_predict import predict
from concurrent.futures import ThreadPoolExecutor
import argparse

def parallel_predict(text):
    return predict(text)

def calculate_avg_sentiment(group):
    return round(group['sentiment_score'].mean(), 3)

def main(input_file, output_reviews_file, output_avg_sentiment_file, num_threads):
    df = pd.read_csv(input_file)

    # Calculate sentiment scores using the predict() function
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
         df['sentiment_score'] = list(executor.map(parallel_predict, df['review_text']))
    df.to_csv(output_reviews_file, index=False)

    # Calculate average sentiment scores for each game title
    df_avg_sentiment = df.groupby('app_name').apply(calculate_avg_sentiment).reset_index()
    df_avg_sentiment.columns = ['app_name', 'avg_sentiment']

    # Output DataFrame with app_name and avg_sentiment for each game title
    df_avg_sentiment.to_csv(output_avg_sentiment_file, index=False)

    print(f"Sentiment analysis completed. Results saved to '{output_reviews_file}' and '{output_avg_sentiment_file}'.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Calculates sentiment score for each review of a game and calculates average score')
    parser.add_argument('--input', dest='input_file', type=str, help='Input file path')
    parser.add_argument('--output_reviews', dest='output_reviews_file', type=str, help='Output .csv file with all reviews and sentiment scores')
    parser.add_argument('--output_avg', dest='output_avg_sentiment_file', type=str, help='Output .csv file with average sentiment scores for each game')
    parser.add_argument('-threads', dest='num_threads', type=int, default=4, help='Number of threads')
    args = parser.parse_args()

    main(args.input_file, args.output_reviews_file, args.output_avg_sentiment_file, args.num_threads)
