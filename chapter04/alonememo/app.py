from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.jungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    result = list(db.articles.find({}, {'_id':False}))
    return jsonify({'result':'success', 'articles': result})

@app.route('/memo', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')['content']
    og_title = soup.select_one('meta[property="og:title"]')['content']
    og_description = soup.select_one('meta[property="og:description"]')['content']

    article = {
        'url' : url_receive,
        'title' : og_title, 
        'description' : og_description,
        'image' : og_image,
        'comment' : comment_receive
    }

    db.articles.insert_one(article)

    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

