"""
Flask server for time.com "The Brief" section API
@author aarushibhatia
@licence MIT License
"""

from flask import Flask, jsonify

import feeds


app = Flask(__name__)

@app.route("/getTimeNews")
def get_news():
    """API end point for News Feed Request"""
    news_response = feeds.news_feed_json()

    return jsonify({
        "news": news_response
    })

# Test API
@app.route("/ok")
def ohkay():
    return jsonify({
        "ok": True
    })

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port="8000")
