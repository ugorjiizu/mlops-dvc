import os
import wget
import requests
import zipfile
import pandas as pd

# Download the zipped dataset
url_train = 'https://drive.google.com/file/d/1_lR9J9bzi27mFd4YtG9v-uyYQrsLTQjn/view?usp=sharing'
url_test = 'https://drive.google.com/file/d/1peJn4OCxBqlXgGFrRHneBuJ7IIWLIqaq/view?usp=sharing'


train_path='https://drive.google.com/uc?id=' + url_train.split('/')[-2]
test_path='https://drive.google.com/uc?id=' + url_test.split('/')[-2]

df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)

df_train.to_csv('train.csv', index=False)
df_test.to_csv('test.csv', index=False)
