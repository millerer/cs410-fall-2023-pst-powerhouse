# Information Retrieval Evaluation Test
This Test is based off the cranfield method for IR evaluation. It calculates the precision, recall, and F-measure for our dataranking function.

To run, execute the file `rank_dataset_test.py`.

# Test Data Sources
Given the format of our expected data, the original cranfield dataset (http://ir.dcs.gla.ac.uk/resources/test_collections/cran/) couldn't be used as-is. However the approach is similar, with a test dataset, query dataset, and 'qrels' dataset (contatining the query number, document number, and relevancy) used in tandem.

The original source for the test data files is [CS 410 assignment 2.1](https://github.com/CS410fa23-Assignment/MP2.1). They have been modfied to more closely match the game review dataset.