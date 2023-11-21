from flair.nn import Classifier
from flair.data import Sentence
from segtok.segmenter import split_single

classifier = Classifier.load('sentiment')

def predict(sentence):
    """ Predict the sentiment of a sentence """
    if sentence == "":
        return 0
    text = Sentence(sentence)
    # stacked_embeddings.embed(text)
    classifier.predict(text)
    try:
        value = text.labels[0].to_dict()['value'] 
        if value == 'POSITIVE':
            result = text.to_dict()['labels'][0]['confidence']
        else:
            result = -(text.to_dict()['labels'][0]['confidence'])
        return round(result, 3)
    except IndexError:
        return 0


def normalize_predictions(score):
    """Normalize the raw Flair score to [-1, 1]"""
    if score > 0:
        return 1
    else:
        return -1