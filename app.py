from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    url = "https://www.businesstoday.in/technology/news"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    #outerData = soup.find_all("div",class_="widget-listing",limit=6)
    #print(outerData)
    finalNews=""
    for data in soup.find_all("div",class_="widget-listing",limit=6):
        news=data.div.div.a["title"]
        finalNews += '\u2022 '+news+'\n'
    #print(finalNews)
    return render_template("index.html",News=finalNews)



