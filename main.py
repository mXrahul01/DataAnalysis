import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Load the dataset
dataset_path = r'C:\Users\LENOVO\Downloads\Dataset1 .csv'
df = pd.read_csv(dataset_path)

# Analyze the text reviews
sia = SentimentIntensityAnalyzer()

# Calculate sentiment scores using the SentimentIntensityAnalyzer
df['Sentiment Score'] = df['Rating text'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Identify positive and negative reviews based on sentiment score
positive_reviews = df[df['Sentiment Score'] >= 0]['Reviews']
negative_reviews = df[df['Sentiment Score'] < 0]['Reviews']

# Tokenize and process reviews
stop_words = set(stopwords.words('english'))

def process_reviews(reviews):
    all_words = []
    for review in reviews:
        words = word_tokenize(str(review).lower())
        words = [word for word in words if word.isalnum() and word not in stop_words]
        all_words.extend(words)
    return all_words

# Process positive and negative reviews
positive_words = process_reviews(positive_reviews)
negative_words = process_reviews(negative_reviews)

# Identify most common positive and negative keywords
most_common_positive_keywords = Counter(positive_words).most_common(10)
most_common_negative_keywords = Counter(negative_words).most_common(10)

print("\nMost Common Positive Keywords:")
print(most_common_positive_keywords)

print("\nMost Common Negative Keywords:")
print(most_common_negative_keywords)

# Calculate the average length of reviews
df['Review Length'] = df['Reviews'].apply(lambda x: len(word_tokenize(str(x))))
average_review_length = df['Review Length'].mean()
print("\nAverage Review Length:", round(average_review_length, 2), "words")

# Explore the relationship between review length and rating
plt.figure(figsize=(10, 6))
plt.scatter(df['Review Length'], df['Aggregate rating'], alpha=0.5)
plt.title('Relationship between Review Length and Rating')
plt.xlabel('Review Length (words)')
plt.ylabel('Aggregate Rating')
plt.show()
