# Twitter Sentiment Analysis Project

## Project Overview
This project performs **sentiment analysis** on a set of sample tweets. The goal is to determine how positive or negative each tweet is based on predefined lists of positive and negative words.

The workflow includes:

1. **Cleaning tweets:** Removing punctuation from words.  
2. **Calculating sentiment scores:**  
   - **Positive Score:** Number of positive words in the tweet.  
   - **Negative Score:** Number of negative words in the tweet.  
   - **Net Score:** Positive Score minus Negative Score.  
3. **Saving results:** Creating a CSV file `resulting_data.csv` with the following columns:  
   - Number of Retweets  
   - Number of Replies  
   - Positive Score  
   - Negative Score  
   - Net Score  
4. **Visualization** The scatter plot showing **Net Score vs Number of Retweets** is also included in the Excel file:
   - `RetweetsVsNeScore.xlsx` – Contains the scatter plot of Net Score against Number of Retweets for all tweets.
---

## Files Included

- `project_twitter_data.csv` – Original sample tweets with retweets and replies.  
- `positive_words.txt` – List of positive words for sentiment analysis.  
- `negative_words.txt` – List of negative words for sentiment analysis.  
- `resulting_data.csv` – Output CSV with sentiment scores and Net Score.  
- `assignment.ipynb` – Code for reading, processing, and analyzing tweets.  
- `NetScore_vs_Retweets.xlsx` – Excel file containing the scatter plot of Net Score vs Number of Retweets.
