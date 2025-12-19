import requests
import csv
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
INSTAGRAM_USER_ID = os.getenv("IG_USER_ID")

if not ACCESS_TOKEN:
    raise ValueError("Missing ACCESS_TOKEN in .env")

if not INSTAGRAM_USER_ID:
    raise ValueError("Missing IG_USER_ID in .env (must be numeric IG user id)")

# API version
BASE_URL = "https://graph.facebook.com/v21.0"


def parse_ig_timestamp(ts: str) -> str:
    """
    Normaliza timestamp do Instagram para ISO local-friendly.
    Mantém como string ISO para CSV (mais compatível).
    """
    try:
        # Ex.: "2025-12-16T12:34:56+0000" ou "...Z"
        ts = ts.replace("Z", "+00:00")
        dt = datetime.fromisoformat(ts.replace("+0000", "+00:00"))
        return dt.isoformat()
    except Exception:
        return ts


def get_posts(limit: int = 50, max_pages: int = 10):
    """
    Busca posts/reels do Instagram com paginação.
    limit: quantos itens por página
    max_pages: limite de páginas para evitar loop infinito
    """
    url = f"{BASE_URL}/{INSTAGRAM_USER_ID}/media"
    params = {
        "fields": "id,caption,media_type,media_url,permalink,timestamp",
        "limit": limit,
        "access_token": ACCESS_TOKEN
    }

    all_posts = []
    pages = 0

    while url and pages < max_pages:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        all_posts.extend(data.get("data", []))

        # paginação do Graph API vem em "paging.next"
        url = data.get("paging", {}).get("next")
        params = None  # quando usa paging.next, não precisa reenviar params

        pages += 1

    return all_posts


def get_insights(media_id: str) -> dict:
    """
    Busca métricas de um post específico.
    Se falhar (métrica indisponível/permissão), retorna {} sem quebrar o script.
    """
    url = f"{BASE_URL}/{media_id}/insights"
    params = {
        "metric": "impressions,reach,likes,comments,saves,shares",
        "access_token": ACCESS_TOKEN
    }

    response = requests.get(url, params=params)

    # Em vez de matar o programa, seguimos com o resto
    if response.status_code != 200:
        return {}

    insights = {}
    for item in response.json().get("data", []):
        # Graph API retorna values como lista
        values = item.get("values", [])
        if values:
            insights[item.get("name")] = values[0].get("value", 0)

    return insights


def export_to_csv(rows: list) -> str:
    """
    Exporta dados para CSV.
    """
    filename = f"instagram_insights_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"

    headers = [
        "post_id",
        "caption",
        "media_type",
        "timestamp",
        "impressions",
        "reach",
        "likes",
        "comments",
        "saves",
        "shares",
        "permalink"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    return filename


def main():
    posts = get_posts(limit=50, max_pages=10)
    all_data = []

    for post in posts:
        post_id = post.get("id")
        if not post_id:
            continue

        insights = get_insights(post_id)

        row = {
            "post_id": post_id,
            "caption": post.get("caption", "").replace("\n", " ").strip(),
            "media_type": post.get("media_type", ""),
            "timestamp": parse_ig_timestamp(post.get("timestamp", "")),
            "impressions": insights.get("impressions", 0),
            "reach": insights.get("reach", 0),
            "likes": insights.get("likes", 0),
            "comments": insights.get("comments", 0),
            "saves": insights.get("saves", 0),
            "shares": insights.get("shares", 0),
            "permalink": post.get("permalink", "")
        }

        all_data.append(row)

    filename = export_to_csv(all_data)
    print(f"✅ Arquivo gerado: {filename}")
    print(f"✅ Posts exportados: {len(all_data)}")


if __name__ == "__main__":
    main()