import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS # Needed to allow the HTML to talk to the server

# --- Setup ---
app = Flask(__name__, static_folder='.', template_folder='.')
# This allows your HTML file (running locally) to make requests to the server
CORS(app)
analyzer = SentimentIntensityAnalyzer()

# --- Load your sample data ---
# This section is updated to load your specific file and column
try:
    # 1. Try to read your new CSV file
    df = pd.read_csv('Untitled spreadsheet - Sheet4.csv') 
    
    # 2. Try to get the list of comments from the 'Comment' column
    comments = df['Comment'].tolist()

except FileNotFoundError:
    # This runs if 'extracted.csv' isn't in the same folder
    comments = ["Error: Could not find extracted.csv.", "Please make sure the file is in the same folder as app.py."]
except KeyError:
    # This runs if 'extracted.csv' is found, but the 'Comment' column doesn't exist
    comments = ["Error: Found 'extracted.csv', but could not find a column named 'Comment'.", "Please check your CSV file's column headers."]
except Exception as e:
    # A catch-all for other potential errors
    comments = [f"An unexpected error occurred: {e}"]


# --- VADER Analysis Function ---
def analyze_comments(comment_list):
    """Analyzes a list of comments and calculates overall sentiment."""
    positive_count = 0
    total_comments = len(comment_list)

    if total_comments == 0:
        return 0.0, 0.0

    for comment in comment_list:
        # VADER needs a string, so we convert just in case
        vs = analyzer.polarity_scores(str(comment)) 
        
        # VADER gives 'compound' score. A common threshold is > 0.05 for positive.
        if vs['compound'] >= 0.05:
            positive_count += 1
    
    # Calculate overall positive sentiment percentage
    sentiment_percentage = (positive_count / total_comments) * 100
    
    # *** DEMO ENGAGEMENT ***
    # Since we don't have real engagement data, we simulate it based on sentiment
    engagement_rate = sentiment_percentage * 0.95 + 5 # 95% of sentiment + a base of 5
    engagement_rate = min(engagement_rate, 99.9) # Cap at 99.9%
    
    return sentiment_percentage, engagement_rate

# --- Flask Route ---
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json(silent=True) or {}
    text = (data.get('text') or '').strip()

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    sentiment = 'Neutral'

    if compound >= 0.4:
        sentiment = 'Very Positive'
    elif compound >= 0.1:
        sentiment = 'Positive'
    elif compound <= -0.4:
        sentiment = 'Very Negative'
    elif compound <= -0.1:
        sentiment = 'Negative'

    return jsonify({
        'sentiment': sentiment,
        'score': round(compound, 3),
        'text': text
    })


@app.route('/analyze', methods=['GET'])
def get_analysis():
    """Returns the analysis results as JSON."""
    
    # In a real app, you would use the URL parameter (e.g., request.args.get('url')) 
    # to fetch new data. For this demo, we use the static dataset.
    
    sentiment_pct, engagement_pct = analyze_comments(comments)

    # Determine the reception type based on sentiment
    if sentiment_pct >= 70:
        reception = 'positive'
        title = 'Highly Positive Reception'
        icon = 'fa-smile-beam'
    elif sentiment_pct >= 40:
        reception = 'mixed'
        title = 'Mixed Audience Opinion'
        icon = 'fa-meh'
    else:
        reception = 'negative'
        title = 'Negative Reception'
        icon = 'fa-frown'

    # Prepare the final data structure
    result = {
        'type': reception,
        'icon': icon,
        'title': title,
        'description': f'Analysis based on {len(comments)} sample comments.',
        'sentiment': round(sentiment_pct, 1),
        'engagement': round(engagement_pct, 1),
        'likes': 1500, # Placeholder for demo
        'views': 25000 # Placeholder for demo
    }

    return jsonify(result)

# --- Run Server ---
if __name__ == '__main__':
    # Runs the server on http://127.0.0.1:5000/
    app.run(debug=True)