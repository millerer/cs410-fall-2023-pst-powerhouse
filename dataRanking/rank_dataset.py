import pandas as pd
from rank_bm25 import BM25Okapi


def rank_dataset(dataset, query):
    """
    Ranking function for a dataset. Based on the Okapi BM25 algorithm.

    Args:
        dataset: A clean dataset (stopwords removed, all lowercase, stemming performed, etc)
        query: User query for searching the dataset

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
    return df.sort_values(by='rank', ascending=False)