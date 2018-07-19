from bs4 import BeautifulSoup as bs
import requests
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
print(stop_words)
