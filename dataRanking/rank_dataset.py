import pandas as pd
import numpy as np
from rank_bm25 import BM25Okapi


def rank_dataset(dataset, query, count=10):
    """
    Ranking function for a dataset. Based on the Okapi BM25 algorithm.

    Args:
        dataset: A clean dataset (stopwords removed, all lowercase, stemming performed, etc)
        query: User query for searching the dataset
        count: Number of top n results to return (default 10)

    Returns:
        The dataset sorted by an additional 'rank' column in desc order
    """
    ## Tokenize the corpus
    tokenzied_corpus = [doc.split(" ") for doc in dataset.review_text]

    ## Create the document index from the corpus
    bm25 = BM25Okapi(tokenzied_corpus)

    # Tokenize the query
    tokenized_query = query.split(" ")

    # Score the documents using okapi bm25
    doc_scores = bm25.get_scores(tokenized_query)

    # Modify the original dataset to include the document rankings
    df = pd.DataFrame(dataset)
    df['rank'] = doc_scores

    # Return the dataset sorted by 'rank' in desc order
    ranked_results = df.groupby(['app_name'], as_index=False).agg(rank=('rank', 'sum'))
    return ranked_results.sort_values(by='rank', ascending=False).head(count)