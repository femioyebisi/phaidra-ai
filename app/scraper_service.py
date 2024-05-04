from flask import Flask, request, jsonify
from prometheus_client import Counter, start_http_server
import requests

app = Flask(__name__)
http_get = Counter('http_get', 'Count of HTTP GET requests', ['url', 'code'])

@app.route('/', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'Missing URL'}), 400
    try:
        response = requests.get(url)
        http_get.labels(url, str(response.status_code)).inc()
        return str(response.status_code), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    start_http_server(9095)
    app.run(host='0.0.0.0', port=8080)
    
