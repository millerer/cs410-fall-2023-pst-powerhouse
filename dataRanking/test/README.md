# Information Retrieval Evaluation Test
This Test is based off the cranfield method for IR evaluation. It calculates the (Macro) precision, recall, and F-measure for our dataranking function.

To run, execute the file `rank_dataset_test.py`.

# Test Data Sources
Given the format of our expected data, the original cranfield dataset (http://ir.dcs.gla.ac.uk/resources/test_collections/cran/) couldn't be used as-is. However this approach is similar, with a test dataset, query dataset, and 'qrels' dataset (contatining the query number, document number, and relevancy) used in tandem.

500 reviews are used for the test documents, which were randomly selected from the data set. To save time, the content has been pre-scrubbed for stop words and stemming. This is also done in our program code before text retrieval and ranking.