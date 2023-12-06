import pandas, nltk, random
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from dataIngestion.dataset_clean import cleaning

# Just give you some idea of the word distribution
def word_cloud_show(review):
    txt = ' '.join(rev for rev in review.review_text)
    plt.figure(figsize=(15, 8))

    wordcloud = WordCloud(
        background_color='black',
        max_font_size=100,
        max_words=100,
        width=1000,
        height=600
    ).generate(txt)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    p = 0.02
    review = pandas.read_csv('../dataIngestion/dataset.csv', skiprows=lambda i: i > 0 and random.random() > p)
    print(review.head())
    print(review.tail())
    review.review_text = review.review_text.astype('str')

    # word_cloud_show(review)
    print("Shape before cleaning : " + str(review.shape))

    # Below code are to clean data.
    cleaning(review, 'review_text')
    # Drop the rows with too short review_text. Feel free to Change the minimum len, 1,  as you like.
    review = review[review['review_text'].map(len) > 1]

    # Print some samples
    print("Shape after cleaning : " + str(review.shape))
    print(review[['review_text']].head(10))

    print("Saving clean dataset to dataset.cleaned.csv")
    review.to_csv('dataset.cleaned.csv')
