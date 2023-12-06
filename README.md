# CS410 Fall 2023 Project for Team PST Powerhouse
This is the group project repository for team PST Powerhouse. It is a recommendation tool for video game titles.

| Project Content  | Video Game Recommendation Tool                                                                                                                                         |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project Topic    | Free Topic                                                                                                                                                             |
| Class/Semester   | CS-410 / Fall 2023                                                                                                                                                     |
| Group Name       | PST Powerhouse                                                                                                                                                         |
| Group Members    | elm3, arjun12, ml171, yongy3, ganesan83                                                                                                                                |
| Project Proposal | See: [Team PST Powerhouse Project Proposal.pdf](https://github.com/millerer/cs410-fall-2023-pst-powerhouse/blob/main/Team%20PST%20Powerhouse%20Project%20Proposal.pdf) |

## 1. An overview of the function of the code
This project is a video game recommendation system which provides a list of game titles based on a user's query and the reviewer sentiment for each game (positive sentiment giving a higher weight).
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
Concerning the ranking process, we tokenize the corpus and input it into the bm25 ranking algorithm to generate scores. 
For recommendations, flair sentiment analysis is implemented and applied to the sentences in the corpus reviews. Ultimately, the top 10 games are generated based on positive sentiment and the highest ranked scores.
For GUI, JScript is used to implement the webpage hosting service.
[TODO - Add more details how the software is implemented here]

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
5. Run the ranking example program in command line.
````
% cd cs410-fall-2023-pst-powerhouse/dataRanking
% python3 rank_dataset_example.py <YOUR_QUERY>
````
Here below shows an example of ranked output for query `Monday`.
````
 % python3 rank_dataset_example.py Monday
Cleaning data...
Ranking....
Top 10 ranked reviews + title
                        app_name       rank
4783   Super Monday Night Combat  21.360585
3543                    POSTAL 2  20.445648
3903             Randal's Monday  16.469592
461                 Awesomenauts  13.273520
1210                        DOOM   8.215752
5822  Yet Another Zombie Defense   7.633979
3665                PlanetSide 2   7.423704
3175         Monday Night Combat   7.036092
2767                        LYNE   7.036092
3093                     Memoria   6.525055
````

### 3.2 How to run the program
As a user, you can input your query from our UI webpage. [TODO add UI link here]. 
It gives you the recommendation of games relevant to your query.

## 4. Contribution of each team member

| Team Member (alias) | Brief description of contribution                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------|
| elm3                | Implemented ranking Okapi BM25, main entry function and testing for ranking. Also coordinated meeting/discussion as group captain. |
| arjun12             | Created and implemented GUI frontend, and end-to-end integration.                                                                  |
| ml171               | Implemented sentiment analysis, added test script and ran tests.                                                                   |
| yongy3              | The dataset choosing, data retrieval & ingestion, data cleaning implementation and documentation.                                  |
| ganesan83           | UI work, deployment and coordination with arjun12 for frontend integration.                                                        |


