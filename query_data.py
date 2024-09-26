# query_data.py
from elasticsearch import Elasticsearch

# Initialize Elasticsearch client
es = Elasticsearch()

# Function to search tweets by a term
def search_term(term):
    query = {
        "query": {
            "match": {
                "text": term
            }
        }
    }
    return es.search(index="tweets", body=query)

# Count tweets per day
def tweets_per_day(term):
    query = {
        "query": {
            "match": {
                "text": term
            }
        },
        "aggs": {
            "tweets_by_day": {
                "date_histogram": {
                    "field": "date",
                    "calendar_interval": "day"
                }
            }
        }
    }
    result = es.search(index="tweets", body=query)
    return result['aggregations']['tweets_by_day']['buckets']

# Count unique users who tweeted
def unique_users(term):
    query = {
        "query": {
            "match": {
                "text": term
            }
        },
        "aggs": {
            "unique_users": {
                "terms": {
                    "field": "user_id"
                }
            }
        }
    }
    result = es.search(index="tweets", body=query)
    return len(result['aggregations']['unique_users']['buckets'])

# Average number of likes
def avg_likes(term):
    query = {
        "query": {
            "match": {
                "text": term
            }
        },
        "aggs": {
            "average_likes": {
                "avg": {
                    "field": "likes"
                }
            }
        }
    }
    result = es.search(index="tweets", body=query)
    return result['aggregations']['average_likes']['value']

# Get place IDs of tweets
def tweet_places(term):
    query = {
        "query": {
            "match": {
                "text": term
            }
        },
        "aggs": {
            "places": {
                "terms": {
                    "field": "place_id"
                }
            }
        }
    }
    result = es.search(index="tweets", body=query)
    return [bucket['key'] for bucket in result['aggregations']['places']['buckets']]

# Time of day tweets were posted
def tweets_by_time(term):
    query = {
        "query": {
            "match": {
                "text": term
            }
        },
        "aggs": {
            "tweets_by_hour": {
                "date_histogram": {
                    "field": "time",
                    "calendar_interval": "hour"
                }
            }
        }
    }
    result = es.search(index="tweets", body=query)
    return result['aggregations']['tweets_by_hour']['buckets']

# User who posted the most tweets
def top_user(term):
    query = {
        "query": {
            "match": {
                "text": term
            }
        },
        "aggs": {
            "top_user": {
                "terms": {
                    "field": "user_id",
                    "size": 1
                }
            }
        }
    }
    result = es.search(index="tweets", body=query)
    return result['aggregations']['top_user']['buckets'][0]['key']
