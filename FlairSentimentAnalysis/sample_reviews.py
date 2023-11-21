import pandas as pd
import numpy as np
import argparse
import sys

sys.path.append('../')
from dataIngestion.dataset_clean import remove_EAR

def sample_reviews(group, N):
    if len(group) > N:
        return group.sample(N, random_state=1)  # Use a fixed random state for reproducibility
    else:
        return group

def main(N, input_file, output_file):
    df = pd.read_csv(input_file)
    df['review_text'].fillna('', inplace=True)
    df['review_text'] = df['review_text'].apply(remove_EAR) # Remove Early Access Review
    df = df[df['review_text'].str.strip() != '']  # Remove all rows with empty review_text

    # Group by 'app_name' and apply the sampling function
    sampled_df = df.groupby('app_name', group_keys=False).apply(lambda group: sample_reviews(group, N))

    # Save the sampled DataFrame to the output CSV file
    sampled_df.to_csv(output_file, index=False)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Produces an output .csv file containg N randomly sampled reviews for each game')
    parser.add_argument('--input', dest='input_file', type=str, help='Input file path')
    parser.add_argument('--output', dest='output_file', type=str, help='Output file path')
    parser.add_argument('-N', dest='N', type=int, default=100, help='Number of reviews per game')
    args = parser.parse_args()

    main(args.N, args.input_file, args.output_file)

