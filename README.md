# CS410 Fall 2023 Project for Team PST Powerhouse
This is the group project repository for team PST Powerhouse. It is a recommendation tool for video game titles.

| Project Content  | Video Game Recommendation Tool                                                                                                                                         |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project Topic    | Free Topic                                                                                                                                                             |
| Class/Semester   | CS-410 / Fall 2023                                                                                                                                                     |
| Group Name       | PST Powerhouse                                                                                                                                                         |
| Group Members    | elm3, arjun12, ml171, yongy3, ganesan83                                                                                                                                |
| Project Proposal | See: [Team PST Powerhouse Project Proposal.pdf](https://github.com/millerer/cs410-fall-2023-pst-powerhouse/blob/main/Team%20PST%20Powerhouse%20Project%20Proposal.pdf) |

# Video Tutorial
[Use this link for the video tutorial](https://www.youtube.com/watch?v=mq-7_20n9X0). This video covers the project contents, setup, and shows an example query.

## 1. An overview of the function of the code
This project is a video game recommendation system which provides a list of game titles based on a user's query and the reviewer sentiment for each game.
Upon entering a query related to the domain of video games, users will receive a ranked list of topK (10) video game titles ranked on relevance to their query and positive reviewer sentiment.
* dataIngestion - A component for data ingestion and data cleaning.
* dataRanking - A ranking implementation by Okapi BM25
* FlairSentimentAnalysis - Sentiment analysis on review texts of dataset, generate Precise, Recall and F1 scores. It also predicates the sentiment for given sentence by Flair. 
* UI - Front end component that provides a Web GUI for user input query and output ranked games as recommendation.
## 2. How the software is implemented
The Python language is utilized for implementing functions, leveraging popular libraries such as rank-bm25 for ranking and flair for sentiment analysis. 
We developed the data cleaning code in-house, which involves the removal of unnecessary hyperlinks, markup, numbers, symbols, punctuation, and stop words. 
Additionally, we apply stemming, convert to lowercase, and standardize whitespaces. We successfully eliminated a specific high-frequency term, "Early Access Review," 
resulting in a significant improvement in accuracy through these data cleaning techniques.
Concerning the ranking process, we tokenize the corpus and input it into the bm25 ranking algorithm to generate scores. Ranking scores are calculated for each of the reviews, then aggregated for each game title.
For recommendations, flair sentiment analysis is implemented and applied to the sentences in the corpus reviews. Ultimately, the top 10 games are generated based on positive sentiment and the highest ranked scores.
For GUI, tkinter is used to implement the webpage hosting service.

### Testing of sentiment analysis
In order to improve the query performance of the search engine, we utilized a random sample of game reviews with a specified size, denoted as N, for calculating the average sentiment of game titles. Employing the entire set of reviews for each game title would be too time-consuming, so we opted for a N value of 10 to ensure quick query turnaround time. 

Subsequently, we conducted a comparative analysis to calculate the average sentiment values with two different sample sizes: a much larger N value of 100 and our chosen N value of 10 to assess the variations in average sentiment across all game titles in the dataset. The average of the differences across all game titles turned out to be 0.011, which is quite small. The distributions of the differences in average sentiment scores are presented below:

![Sentiment Differences Histogram](/FlairSentimentAnalysis/output/N100-N10_sentiment_distributions.png)

Please refer to `sentimentTest/compare_avg_sentiment.ipynb` for the full analysis. In order to generate the average sentiment values for all game titles with a given N value, use the `FlairSentimentAnalysis\avg_sentiment_for_all_games.py` script:

~~~~
python FlairSentimentAnalysis\avg_sentiment_for_all_games.py --input [dataIngestion/dataset.csv] --output [output .csv file path] --threads [number of threads] -N [N value]
~~~~

### Testing of Retrieval Performance
In order to judge our game title ranker's retrival performance, we used a variation of the cranfield relevancy experiments. A set of ten queries (`test_queries.txt`) was manually compared against a sampling of 500 reviews (`test_reviews.txt`) for relevancy. The results from this manual 'ideal result' set were then recorded into a file (`test_qrels.csv`). We then created a test script that compared the expected relevant documents to documents that the ranking function claimed were relevant (threshold of 0 being used for relevancy). Calculating the macro average precision, recall, and F1 score had the following results:
```
Macro Average Precision: 0.9702380952380951, Macro Average Recall: 0.5586309523809524, Macro Average F1 Measure: 0.6421254399195576
```
The macro average precision was very high for the query set, with a lower recall. This gives us confidence that retrieved documents will likely be relevant to a query, but that some relevant results may be missed. Further manual testing of the application against the entirety of the corpus seemed to indicate that this was the case. However given the huge size of the dataset, missing some relevant results is not as large a concern.

To run the tests for retrieval, use the `retieval_test.py` script.

## 3. Usage of the software
### 3.1 How to install
1. This requires python 3.9+ to run. (Later version may still work, but unverified). Please download Python installer from https://www.python.org/downloads/release/python-390/
* Optionally you can install PyCharm IDE. Download PyCharm from https://www.jetbrains.com/pycharm/
2. Install required packages, you can do either method below.
  * Command line: 
~~~~
% pip3 install pandas numpy nltk rank_bm25 flair
~~~~
  * Install aforementioned packages from PyCharm: (Make sure you select Python 3.9 interpreter upfront)
~~~~
PyCharm -> Settings -> Project -> Python interpreter -> Click '+' button. 
~~~~
3. Clone the project 
~~~~
% git clone git@github.com:millerer/cs410-fall-2023-pst-powerhouse.git
% cd cs410-fall-2023-pst-powerhouse
~~~~
4. Download the [streamreviews dataset](https://www.kaggle.com/datasets/andrewmvd/steam-reviews/)('archive.zip') from [kaggle](https://www.kaggle.com/datasets/andrewmvd/steam-reviews/). 
You have to exact and save it to dataIngestion/ folder in your cloned git project.
````
% unzip ~/Downloads/archive.zip -d dataIngestion/
````
5. Run the ranking program from the command line.
````
% cd cs410-fall-2023-pst-powerhouse
% python3 UI.py
````
Here below shows an example of ranked output for query `France`.
![Example Query Results](/ui_example.jpg)

### 3.2 How to run the program
As a user, you can input your query from our UI page. Run `UI.py` from the root directory. You can veiw the actions of the backend from the console. 
It gives you the recommendation of games relevant to your query.

## 4. Contribution of each team member

| Team Member (alias) | Brief description of contribution                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------|
| elm3                | Implemented ranking Okapi BM25, main entry function and testing for ranking. Also coordinated meeting/discussion as group captain. |
| arjun12             | Created and implemented GUI frontend, and end-to-end integration.                                                                  |
| ml171               | Implemented sentiment analysis, added test script and ran tests.                                                                   |
| yongy3              | The dataset choosing, data retrieval & ingestion, data cleaning implementation and documentation.                                  |
| ganesan83           | UI work, deployment and coordination with arjun12 for frontend integration.                                                        |


