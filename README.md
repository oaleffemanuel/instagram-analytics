# Instagram Organic Analytics Dashboard

This project collects and organizes **organic Instagram content metrics** and sends them to a Google Sheet, which serves as the data source for internal dashboards and reporting.

The goal is to centralize organic performance data in a simple, structured, and extensible way, enabling weekly and monthly analysis without relying on third-party tools.

---

## What this project does

- Fetches organic Instagram media (posts and reels)
- Retrieves engagement metrics per content:
  - Views
  - Likes
  - Comments
  - Shares
  - Saves
- Sends the data to a Google Sheet used as a database
- Keeps the process lightweight and automation-ready

This project focuses **only on organic content**. Paid metrics are intentionally excluded.

---

## Tech Stack

- Python 3
- Instagram Graph API
- Google Sheets (Apps Script integration)
- Environment variables for secrets management

---

## Project Structure

instagram_analytics/
│
├── output/
│   └── .gitkeep
│
├── scripts/
│   └── smoke_test.py
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── export_csv.py
│   ├── extract.py
│   ├── instagram_analytics.py
│   └── meta_client.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

---

## Environment Variables

Create a `.env` file based on `.env.example`:

INSTAGRAM_ACCESS_TOKEN=your_access_token_here
INSTAGRAM_USER_ID=your_instagram_user_id_here
GOOGLE_SHEET_URL=your_google_sheet_url_here

Never commit your `.env` file.

---

## How it works

1. Fetches recent Instagram media from the connected business account
2. Retrieves engagement insights for each content
3. Formats the data to match the Google Sheets database
4. Sends the metrics to the sheet for reporting and dashboards

---

## Running locally

Install dependencies:

```bash
pip install -r requirements.txt

Run a connectivity test:

python3 scripts/smoke_test.py

Run the full pipeline:

python3 src/run.py


⸻

Current limitations
	•	Follower growth is tracked manually
	•	Revenue attribution is handled separately
	•	Access tokens must be renewed externally

⸻

Roadmap
	•	Token refresh automation
	•	Weekly and monthly aggregations
	•	Multi-platform support
	•	Dashboard enhancements

⸻

Internal Use

This repository is intended for internal analytics and experimentation.