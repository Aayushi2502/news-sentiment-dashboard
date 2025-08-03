import streamlit as st
import plotly.express as px
from pipeline import fetch_news, clean_and_analyze, tag_topics

from dotenv import load_dotenv
import os

load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

TOPIC_KEYWORDS = {
    "Politics": ["election", "government", "president", "parliament"],
    "Technology": ["AI", "tech", "software", "startup", "cyber"],
    "Economy": ["inflation", "stock", "market", "unemployment", "GDP"],
    "Health": ["covid", "vaccine", "health", "hospital", "medicine"],
    "Environment": ["climate", "environment", "carbon", "pollution"],
}

st.set_page_config(layout="wide")
st.title("Daily News Sentiment Analysis")

with st.spinner("Fetching and analyzing news..."):
    df = fetch_news(query="*", page_size=100, max_pages=10)
    df = clean_and_analyze(df)
    #st.write("Columns in DataFrame:", df.columns.tolist())
    df = tag_topics(df, TOPIC_KEYWORDS)

topics = df['topic'].unique().tolist()
selected_topics = st.sidebar.multiselect("Filter by Topic", options=topics)
filtered_df = df[df['topic'].isin(selected_topics)]

sentiment_trend = (
    filtered_df.groupby(["publishedAt", "topic"])
    .sentiment.mean()
    .reset_index()
)

fig = px.line(
    sentiment_trend,
    x="publishedAt",
    y="sentiment",
    color="topic",
    title="Sentiment Trend by Topic",
    markers=True
)
st.plotly_chart(fig, use_container_width=True)

top_pos = df[df['sentiment'] > 0.5].sort_values(by='sentiment', ascending=False).head(5).reset_index(drop=True)

top_pos.insert(0, 'Rank', range(1, len(top_pos) + 1))

top_pos_display = top_pos.rename(columns={
    'title': 'Title',
    'source': 'Source',
    'sentiment_label': 'Sentiment Label',
    'sentiment': 'Sentiment Score'
})

st.subheader("Top Positive Headlines")
st.dataframe(
    top_pos_display[['Rank', 'Title', 'Source', 'Sentiment Label', 'Sentiment Score']],
    hide_index=True,
    use_container_width=True
)



top_neg = df[df['sentiment'] < -0.5].sort_values(by='sentiment').head(5).reset_index(drop=True)

top_neg.insert(0, 'Rank', range(1, len(top_neg) + 1))

top_neg_display = top_neg.rename(columns={
    'title': 'Title',
    'source': 'Source',
    'sentiment_label': 'Sentiment Label',
    'sentiment': 'Sentiment Score'
})

st.subheader("Top Negative Headlines")
st.dataframe(
    top_neg_display[['Rank', 'Title', 'Source', 'Sentiment Label', 'Sentiment Score']],
    hide_index=True,
    use_container_width=True
)
