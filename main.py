from flask import Flask, request, jsonify
from flask_cors import CORS
from newspaper import Article
from summarize import summarize_content

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/fetch-article', methods=['POST'])
def fetch_article():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL not provided'}), 400
    url = data['url']
    try:
        content = extract_content_from_url(url)
        return jsonify({'article': content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate-summary', methods=['POST'])
def generate_summary():
    data = request.get_json()
    if not data or 'article' not in data:
        return jsonify({'error': 'Article content not provided'}), 400
    content = data['article']
    try:
        summary = summarize_content(content)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def extract_content_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
