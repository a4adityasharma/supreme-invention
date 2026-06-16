# YouTube Sentiment Analyzer (Simple Demo)

This small demo analyzes text (YouTube URLs or titles) with a simple sentiment API backed by VADER and Flask. It is intentionally minimal and meant for local experimentation.

Features:
- Frontend: plain HTML/CSS/JS (modernized theme)
- Backend: Flask + VADER sentiment (via `vaderSentiment`)

Quick start:

1. Create a Python virtual environment and activate it

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
python -m vaderSentiment.vader_lexicon
```

3. Run the app

```bash
python app.py
```

4. Open http://127.0.0.1:5000

Notes:
- This demo uses a static CSV (if present) for bulk-analysis endpoint. Live extraction of YouTube comments is out of scope for the demo.
- If you want help adding features (YouTube scraping, OAuth, persisted storage), ask and I can extend it.
📺 YouTube Video Sentiment Analyzer








🎯 Overview

A modern web application that analyzes the sentiment of YouTube video comments using a video URL or title.

It processes user input and returns whether audience reactions are:

😊 Positive
😐 Neutral
😡 Negative
🖼️ Demo Preview
🔥 Home Interface

📊 Analysis Result

🚀 Features

✔ Analyze YouTube video sentiment
✔ Accepts video URL or title
✔ Clean and modern UI
✔ Fast API-based response
✔ Error handling for invalid input
✔ Fully responsive design

🛠️ Tech Stack
HTML5
CSS3
JavaScript (Vanilla JS)
Fetch API
External Sentiment Analysis API
📂 Project Structure
youtube-sentiment-analyzer/
│
├── index.html        # Main UI
├── style.css         # Styling
├── script.js         # Logic & API calls
└── README.md
⚙️ How It Works
📌 Example Usage
Input:
https://www.youtube.com/watch?v=example
Output:
{
  "sentiment": "Positive",
  "confidence": 0.87,
  "summary": "Most users reacted positively to the video."
}
💻 Getting Started
1️⃣ Clone Repo
git clone https://github.com/your-username/youtube-sentiment-analyzer.git
2️⃣ Open Project

Simply open:

index.html

in your browser.

❗ Error Handling

The app handles:

Invalid YouTube URLs
Empty responses
API failures
Network issues
📈 Future Improvements
🌐 Backend integration (Node.js / Flask)
📊 Sentiment charts & graphs
☁️ Cloud deployment
🧠 Better NLP model accuracy
🌍 Multi-language support
👨‍💻 Author

Your Name
Frontend Developer

📜 License

This project is licensed under the MIT License.

⭐ Support

If you like this project:

⭐ Star the repo
🍴 Fork it
🛠️ Contribute improvements