import os
import wget

DATASET_URL = 'https://www.kaggle.com/datasets/andrewmvd/steam-reviews/download?datasetVersionNumber=3'
def download_dataset(dataset_url):
    try:
        if not os.path.exists("dataIngestion/dataset.csv"):
            # This may not work without Kaggle account logged in. Please download the dataset manually from the dataset_url.
            wget.download(dataset_url)
        print("Dataset file downloaded to 'dataIngestion/dataset.csv'")
    except Exception as e:
        print("Download error occurred: " + str(e))


if __name__ == '__main__':
    download_dataset(DATASET_URL)