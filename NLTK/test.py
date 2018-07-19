##from bs4 import BeautifulSoup as bs
##import requests
##import nltk
##from nltk.stem import WordNetLemmatizer
##
##input = input("Ask me anything : ")
##
##def Definition(question):
##    wnl = WordNetLemmatizer()
##    tokens = nltk.word_tokenize(question)
##    for i in tokens:
##        if i in tokens == "ah" or "lor" or "leh" or "eh":
##            tokens.remove(i)
##    tagged = nltk.pos_tag(tokens)
##    find = []
##    
##    for word, pos in tagged:
##        if pos == 'NN' or pos == 'NNS':
##            word = wnl.lemmatize(word)
##            find.append(word)
##
##    question = "".join(find)
##    firstLetter = question[0]
##    url = 'https://www.investopedia.com/terms/' + firstLetter + '/' + question + '.asp'
##    response = requests.get(url)
##    content = response.text
##    soup = bs(content, 'html.parser')
##    print(soup)
##    ans = soup.find('div', {'class' : 'content-box-term'})
##    ans = ans.find('p')
##    ans = ans.text.strip()
##    return ans
##
##print(Definition(input))

from bs4 import BeautifulSoup as bs
import requests
import nltk
from nltk.stem import WordNetLemmatizer

input = input("Ask me anything : ")

def Definition(question):
    wnl = WordNetLemmatizer()
    tokens = nltk.word_tokenize(question)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
    find = []

    for word, pos in tagged:
        if pos == 'NN' or 'NNS' or 'JJ':
            word = wnl.lemmatize(word)
            find.append(word)

    question = "".join(find)
    firstLetter = question[0]
    url = 'https://www.investopedia.com/terms/' + firstLetter + '/' + question + '.asp'
    response = requests.get(url)
    content = response.text
    soup = bs(content, 'html.parser')
    if soup.find('div', {'class' : 'content-box-term'}) is not None:
        ans = soup.find('div', {'class' : 'content-box-term'})
        ans = ans.find('p')
        ans = ans.text.strip()
    elif soup.find('div',{'class': 'roth__content'}) is not None:
        ans = soup.find('div', {'class': 'roth__content'})
        ans = ans.find('p')
        ans = ans.text.strip()
    return ans

print(Definition(input))


