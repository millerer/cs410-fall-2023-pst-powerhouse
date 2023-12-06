import sys
import os
import pandas as pd, random
import numpy as np
import nltk
import csv

from pathlib import Path
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
sys.path.append(str(Path(__file__).parent.parent.parent))
from dataIngestion.dataset_clean import cleaning, remove_stopword
from dataRanking.rank_dataset import rank_dataset

def build_dataset(sourceFilePath):
    lines = []
    with open(sourceFilePath, 'r') as f:
        for line in f:
            lines.append(line)

    df = pd.DataFrame(lines, columns=["review_text"])
    df['review_text'] = df['review_text'].astype('str')
    df.insert(0, 'app_name', range(1, len(df)+1))
    return df

def build_queries(sourceFilePath):
    lines = []
    with open(sourceFilePath, 'r') as f:
        for line in f:
            lines.append(line)

    df = pd.DataFrame(lines, columns=["query_text"])
    df['query_text'] = df['query_text'][:-1].astype('str') #remove trailing newline
    df = df.dropna(thresh=1)
    df.insert(0, 'query_number', range(1, len(df)+1))
    return df

def build_qrels(sourceFilePath):
    df = pd.read_csv(sourceFilePath)
    return df

if __name__ == '__main__':
    ## Create a dataset in the game review format from review data
    reviews = build_dataset('data/test_reviews.txt')

    ## Parse the queries
    queries = build_queries('data/test_queries.txt')

    ## Parse the 'qrels' data (query_number, doc_number, relevancy)
    qrels = build_qrels('data/test_qrels.csv')

    ## Measure the precision, recall, and f-1 for each query
    precision_values = []
    recall_values = []
    fmeasure_values = []

    for query in queries.to_numpy():
        query_number = query[0]
        query_text = query[1].lower()
        result = rank_dataset(reviews, query_text, len(reviews)-1)
        threshold = 0

        tp = 0 # true positive count
        tn = 0 # true negative count
        fp = 0 # false positive count
        fn = 0 # false negative count
        
        for result in result.to_numpy():
            app_name = result[0]
            rank = result[1]

            relevant_docs = qrels.loc[qrels['query_number'] == query_number]
            is_relevant = len(relevant_docs.loc[relevant_docs['document_number'] == app_name]) > 0
            guessed_relevant = rank > threshold

            if(is_relevant and guessed_relevant):
                tp += 1
            elif(not is_relevant and not guessed_relevant):
                tn += 1
            elif(not is_relevant and guessed_relevant):
                fp += 1
            else:
                fn += 1
            
        if tp > 0:
            precision = tp/(tp+fp)
            recall = tp/(tp+fn)
            f1_measure =  (2*precision*recall)/(precision + recall)
            precision_values.append(precision)
            recall_values.append(recall)
            fmeasure_values.append(f1_measure)
        elif(fp > 0 or fn > 1):
            fmeasure_values.append(0)
            if(fp > 1):
                precision_values.append(0)
            if(fn > 1):
                recall_values.append(0)
    
    ## print the macro average precision, recall, and F1 Measure for all queries
    avg_precision = sum(precision_values)/len(precision_values)
    avg_recall = sum(recall_values)/len(recall_values)
    avg_fmeasure = sum(fmeasure_values)/len(fmeasure_values)

    print("Macro Average Precision: {}, Macro Average Recall: {}, Macro Average F1 Measure: {}" \
        .format(avg_precision,avg_recall,avg_fmeasure))
