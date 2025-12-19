import requests

ACCESS_TOKEN = "IGAAqm7TrCVDtBZAFpzUFRYN2FEU1VKRF9JckdqeEZASZAzV4dm9hYWljRXVTY0xscDlyaEhSTkVFLUt0blU5QTBiOWdJVVA0ZAXVacm83c1Y0MzBtcWd1RExCcFg2ZAVBFeThSSGNCZAWcxbGgxVU5CY2lDNGFSd2dabXdsbWdwN0xENAZDZD"
IG_USER_ID = "adapta_org"
BASE_URL = "https://graph.facebook.com/v18.0"

def main():
    # 1) Testa se o token funciona e se o IG User ID é real/acessível
    url = f"{BASE_URL}/{IG_USER_ID}"
    params = {
        "fields": "id,username,account_type,media_count",
        "access_token": ACCESS_TOKEN
    }
    r = requests.get(url, params=params, timeout=30)
    print("STATUS:", r.status_code)
    print(r.text)

if __name__ == "__main__":
    main()