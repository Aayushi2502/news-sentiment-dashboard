import requests
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

from dotenv import load_dotenv
import os

load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

def fetch_news(query="*", language="en", page_size=100, max_pages=1):
    base_url = "https://newsapi.org/v2/everything"
    headers = {'Authorization': NEWSAPI_KEY}
    params = {
        "q": query,
        "language": language,
        "pageSize": 100,
        "page": 1,
        "sortBy": "publishedAt"
    }

    r = requests.get(base_url, params=params, headers=headers)
    if r.status_code != 200:
        print("Error fetching:", r.text)
        return pd.DataFrame()

    data = r.json().get("articles", [])
    return pd.DataFrame(data)

def clean_and_analyze(df):
    df = df.dropna(subset=['title'])
    df.loc[:,'content_full'] = df['title'] + ' ' + df['description'].fillna('')
    
    def get_sentiment_label(text):
        score = analyzer.polarity_scores(text)['compound']
        if score >= 0.05:
            return score, "Positive"
        elif score <= -0.05:
            return score, "Negative"
        else:
            return score, "Neutral"
    
    sentiment_results = df['content_full'].apply(get_sentiment_label)
    df.loc[:, 'sentiment'] = sentiment_results.apply(lambda x: x[0])
    df.loc[:, 'sentiment_label'] = sentiment_results.apply(lambda x: x[1])
    df.loc[:, 'publishedAt'] = pd.to_datetime(df['publishedAt']).dt.date

    return df

def tag_topics(df, keyword_dict):
    df['topic'] = 'Other'
    for topic, keywords in keyword_dict.items():
        mask = df['content_full'].str.contains('|'.join(keywords), case=False, na=False)
        df.loc[mask, 'topic'] = topic
    return df
