# api.py
from flask import Flask, request, jsonify
import query_data  # Import your query functions

app = Flask(__name__)

# Endpoint for querying tweets
@app.route('/query', methods=['GET'])
def query_term():
    term = request.args.get('term')
    if not term:
        return jsonify({'error': 'Missing search term'}), 400

    data = {
        'tweets_per_day': query_data.tweets_per_day(term),
        'unique_users': query_data.unique_users(term),
        'avg_likes': query_data.avg_likes(term),
        'places': query_data.tweet_places(term),
        'tweets_by_time': query_data.tweets_by_time(term),
        'top_user': query_data.top_user(term)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
