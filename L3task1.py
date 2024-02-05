import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import nltk

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)
# Task 1: Analyze the text reviews
# Calculate sentiment scores using the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
df['Sentiment Score'] = df['Rating text'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Identify positive and negative reviews based on sentiment score
positive_reviews = df[df['Sentiment Score'] >= 0.2]['Reviews']
negative_reviews = df[df['Sentiment Score'] < -0.2]['Reviews']

# Create WordClouds for positive and negative reviews
def generate_wordcloud(reviews, title):
    wordcloud = WordCloud(width=800, height=400, max_words=100, background_color='white').generate(' '.join(reviews))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

generate_wordcloud(positive_reviews, 'WordCloud for Positive Reviews')
generate_wordcloud(negative_reviews, 'WordCloud for Negative Reviews')

# Task 1: Calculate the average length of reviews
df['Review Length'] = df['Reviews'].apply(lambda x: len(str(x).split()))
average_review_length = df['Review Length'].mean()
print("\nAverage Review Length:", round(average_review_length, 2), "words")

# Task 1: Explore the relationship between review length and rating
plt.figure(figsize=(10, 6))
plt.scatter(df['Review Length'], df['Aggregate rating'], alpha=0.5)
plt.title('Relationship between Review Length and Rating')
plt.xlabel('Review Length (words)')
plt.ylabel('Aggregate Rating')
plt.show()
