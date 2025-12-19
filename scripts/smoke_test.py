import requests

ACCESS_TOKEN = "SEU_TOKEN_AQUI"

url = "https://graph.facebook.com/v22.0/me"
params = {
    "access_token": ACCESS_TOKEN
}

r = requests.get(url, params=params)
print("STATUS:", r.status_code)
print(r.text)

from src.meta_client import graph_get
from src.config import BASE_URL, IG_USER_ID

def smoke_test():
    print("🔍 Testando conexão com Meta Graph API...")

    # Teste 1: /me
    me = graph_get(f"{BASE_URL}/me")
    print(f"✔ Conectado como: {me.get('id')}")

    # Teste 2: listar posts
    posts = graph_get(
        f"{BASE_URL}/{IG_USER_ID}/media",
        {"fields": "id,media_type", "limit": 3}
    ).get("data", [])

    print(f"✔ Posts encontrados: {len(posts)}")

    if posts:
        post_id = posts[0]["id"]
        print(f"🔍 Testando insights do post {post_id}")

        insights = graph_get(
            f"{BASE_URL}/{post_id}/insights",
            {"metric": "impressions,reach"}
        )

        print("✔ Insights OK")

    print("✅ Smoke test finalizado com sucesso")

if __name__ == "__main__":
    smoke_test()