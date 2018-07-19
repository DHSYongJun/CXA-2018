import json
import requests
from flask import Flask
from flask import request
import wikipedia

# Flask app should start in global layout
app = Flask(__name__)

CLIENT_ACCESS_TOKEN = "0333266a23244566a358cb15f15acac3"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    dict = req.get("result").get("parameters")
    answer = {}
    if req.get("result").get("action") == "InvestopediaDefinition":
        financialTerm = dict["FinancialTerm"]
        term = checkresult(financialTerm)
        definition = wikipedia.summary(term, sentences=2)
        answer["speech"] = definition
    elif req.get("result").get("action") == "RecentNews":
        Company = dict["Company"]
        symbol = checkCompany(Company)
        URL = "https://api.intrinio.com/news?identifier=" + symbol
        news = requests.get(URL, auth=('4715f1f69a73434e2d17633179fe944b', 'ae73fae697a7f1faa3837c95c827e4cd'))
        news = news.json()['data']
        news = list(news)
        eventList = []
        for i in range(5):
            event = news[i]
            eventList.append(event['title'])
            i += 1
        reply = "Here are the recent headlines about " + Company + ": " + "1. " + eventList[0] + " 2. " + eventList[1] + " 3. " + eventList[2] + " 4. " + eventList[3] + " 5. " + eventList[4]
        answer["speech"] = reply
    res = json.dumps(answer)
    return res


def checkresult(value):
    new = value
    if value == "atm" or "ATM" is True:
        new = "Automated teller machine"
    elif value == "equity" or "equities" is True:
        new = "Equity (finance)"
    elif value == "blue chip":
        new = "Blue chip (stock market)"
    elif value == "liability":
        new = "Liability (financial accounting)"
    return new

def checkCompany(value):
    new = value
    if value == "Apple":
        new = "AAPL"
    elif value == "Google":
        new = "GOOGL"
    elif value == "Microsoft":
        new = "MSFT"
    return new