**Daily News Sentiment Dashboard**

A Streamlit-based web app that fetches the latest news articles using the NewsAPI, analyzes their sentiment using TextBlob, and displays interactive charts and top headlines categorized by sentiment.

Features:

- Fetches 100+ daily news articles using **NewsAPI**
- Analyzes sentiment (Positive, Neutral, Negative) using **TextBlob**
- Visualizes sentiment trends using **Plotly**
- Highlights top 5 most positive and negative headlines
- Grouped sentiment by date for time-based insights

Installation:

1. Clone the repository:
   git clone https://github.com/yourusername/news-sentiment-dashboard.git
   cd news-sentiment-dashboard

2. Set up virtual environment:
  python -m venv venv
  venv\Scripts\activate  # On Windows

3. Install Dependencies:
   pip install -r requirements.txt
   
4. Add your API key:
   Create a .env file in the project root:
   NEWSAPI_KEY=your_newsapi_key_here
  # Get your key from https://newsapi.org

5. Run the app:
   streamlit run app.py

