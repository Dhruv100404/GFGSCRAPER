# import streamlit as st
# from flask import Flask, request, jsonify
# import requests
# from bs4 import BeautifulSoup

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return st.title("GFG Scraper")

# @app.route('/scrape', methods=['POST'])
# def scrape():
#     input_url = request.json.get('url')

#     response = requests.get(input_url)
#     soup = BeautifulSoup(response.content, "html.parser")

#     title = soup.find("h1").get_text()

#     article_text = soup.find("div", class_="text")
#     para = article_text.find_all(["p", "h2", "h3", "span"], recursive=False)
#     paragraphs = [paragraph.get_text() for paragraph in para if paragraph.name != "pre"]

#     result = {
#         'title': title,
#         'paragraphs': paragraphs
#     }

#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        input_url = request.json.get('url')
        response = requests.get(input_url)
        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.find("h1").get_text()

        article_text = soup.find("div", class_="text")
        para = article_text.find_all(["p", "h2", "h3", "span"], recursive=False)
        paragraphs = [p.get_text() for p in para if p.name != "pre"]

        result = {
            'title': title,
            'content': paragraphs
        }

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
