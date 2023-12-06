import pandas as pd
import re
import nltk
import os
import ssl

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

pd.options.display.max_rows = None

def clean_hyperlinks_and_markup(raw):
    """ Remove hyperlinks and markup """
    result = re.sub("<[a][^>]*>(.+?)</[a]>", 'Link.', raw)
    result = re.sub('&gt;', "", result)
    result = re.sub('&#x27;', "'", result)
    result = re.sub('&quot;', '"', result)
    result = re.sub('&#x2F;', ' ', result)
    result = re.sub('<p>', ' ', result)
    result = re.sub('</i>', '', result)
    result = re.sub('&#62;', '', result)
    result = re.sub('<i>', ' ', result)
    result = re.sub("\n", '', result)
    return result


def remove_num(texts):
    """ Remove numeric """
    output = re.sub(r'\d+', '', texts)
    return output


def deEmojify(x):
    """ Remove emojis """
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', x)


def unify_whitespaces(x):
    """ Unify whilespaces """
    cleaned_string = re.sub(' +', ' ', x)
    return cleaned_string


def remove_symbols(x):
    """ remove symbols """
    cleaned_string = re.sub(r"[^a-zA-Z0-9?!.,]+", ' ', x)
    return cleaned_string


def remove_punctuation(text):
    """ Remove punctuation """
    final = "".join(u for u in text if u not in ("?", ".", ";", ":", "!", '"', ','))
    return final

def remove_stopword(text):
    """ Remove stopwords """
    stop = set(stopwords.words("english"))
    text = [word.lower() for word in text.split() if word.lower() not in stop]
    return " ".join(text)


def stemming(text):
    """ word stemming """
    snowball_stemmer = SnowballStemmer('english')
    word_tokens = nltk.word_tokenize(text)
    stemmed_word = [snowball_stemmer.stem(word) for word in word_tokens]
    stem = ' '.join(stemmed_word)
    return stem

def remove_EAR(x):
    """ Remove those review with 'Early Access Review' only """
    cleaned_string = re.sub(r"earl[iy] access review", '', x, flags=re.IGNORECASE)
    return cleaned_string

def cleaning(df, review):
    """ Main cleaning function that combining all """
    if not os.path.exists(os.path.expanduser('~/nltk_data')):
        # This is to workaround NLTK downloading error due to SSL certificate. Refer to https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context
        # Download stopwords if not already.
        nltk.download('stopwords')
    df[review] = df[review].apply(clean_hyperlinks_and_markup)
    df[review] = df[review].apply(deEmojify)
    df[review] = df[review].str.lower()
    df[review] = df[review].apply(remove_num)
    df[review] = df[review].apply(remove_symbols)
    df[review] = df[review].apply(remove_punctuation)
    df[review] = df[review].apply(remove_stopword)
    #df[review] = df[review].apply(stemming)
    df[review] = df[review].apply(remove_EAR)
    df[review] = df[review].apply(unify_whitespaces)



