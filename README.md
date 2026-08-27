# Daily News Sentiment Dashboard 📰

A Streamlit-based NLP application that **fetches current news articles and analyzes headline sentiment** using TextBlob.

The dashboard categorizes news as positive, neutral, or negative and visualizes sentiment patterns through interactive charts.

## Features

* Fetches daily news using NewsAPI
* Sentiment analysis with TextBlob
* Positive, Neutral & Negative classification
* Interactive sentiment visualizations
* Top positive and negative headlines
* Date-wise sentiment analysis

## Tech Stack

* Python
* Streamlit
* TextBlob
* NewsAPI
* Plotly
* Pandas

## How It Works

1. Fetches recent news articles using NewsAPI.
2. TextBlob calculates the sentiment of each headline.
3. Headlines are classified as Positive, Neutral, or Negative.
4. Results are visualized through an interactive dashboard.
5. The most positive and negative headlines are highlighted.

## Run Locally

```bash id="ng1nss"
git clone https://github.com/YOUR_USERNAME/news-sentiment-dashboard.git
cd news-sentiment-dashboard
pip install -r requirements.txt
streamlit run app.py
```

Add your NewsAPI key to a `.env` file:

```text
NEWSAPI_KEY=your_newsapi_key_here
```

## Future Improvements

* Use transformer-based sentiment models
* Add topic/category filtering
* Compare sentiment across different news sources
* Add historical sentiment trend analysis

## Author

**Aayushi Bhathgara**
Computer Science & Engineering — Artificial Intelligence and Machine Learning
