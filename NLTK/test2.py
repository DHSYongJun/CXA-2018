from bs4 import BeautifulSoup as bs
import requests

input = input("Ask me anything : ")

#wnl = WordNetLemmatizer()
#tokens = nltk.word_tokenize(question)
#tagged = nltk.pos_tag(tokens)
#find = []

#for word, pos in tagged:
#    if pos == 'NN' or pos == 'NNS':
#        word = wnl.lemmatize(word)
#        find.append(word)

question = input.replace(" ", "%20")
url = 'https://www.investopedia.com/search/?search-terms=/' + question
response = requests.get(url)
content = response.text
soup = bs(content, 'html.parser')
ans = soup.find('h3', {'class' : 'result-title'})
print(ans)
for a in ans.find_all('a', href=True):
    url = a['href']
    break

response = requests.get(url)
content = response.text
soup = bs(content, 'html.parser')
ans = soup.find('div', {'class' : 'content-box'})
ans = ans.find('p')
ans = ans.text.strip()
print(ans)
##ans = ans.find('p')
##ans = ans.text.strip()

