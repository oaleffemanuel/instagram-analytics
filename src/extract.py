from src.meta_client import graph_get
from src.config import BASE_URL, IG_USER_ID

def get_posts(limit=10):
    url = f"{BASE_URL}/{IG_USER_ID}/media"
    params = {
        "fields": "id,caption,media_type,permalink,timestamp",
        "limit": limit
    }
    return graph_get(url, params).get("data", [])

def get_insights(media_id):
    url = f"{BASE_URL}/{media_id}/insights"
    params = {
        "metric": "impressions,reach,likes,comments,saves,shares"
    }

    data = graph_get(url, params).get("data", [])

    insights = {}
    for item in data:
        insights[item["name"]] = item["values"][0]["value"]

    return insights