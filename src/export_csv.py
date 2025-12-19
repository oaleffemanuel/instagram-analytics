import csv
from datetime import datetime

def export_to_csv(rows):
    filename = f"output/instagram_insights_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"

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
        "shares"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV gerado: {filename}")