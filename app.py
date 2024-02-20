from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        input_url = request.json.get('url') 
        print("Input URL:", input_url)

        response = requests.get(input_url)
        print("Response Status Code:", response.status_code)

        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.find("h1").get_text()
        print("Title:", title)

        article_text = soup.find("div", class_="text")
        para = article_text.find_all(["p", "h2", "h3", "span"], recursive=False)
        paragraphs = [p.get_text() for p in para if p.name != "pre"]

        result = {
            'content': paragraphs
        }

        return jsonify(result), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
