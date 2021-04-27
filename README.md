# TwitterSentiment
A prototype experiment on the real time sentiment analysis of tweets using PySpark.

# Quick Start

1. Clone repo.
2. Install & activate virtual environment.
    ```
    python3 -m venv env
    source env/bin/activate
    ```
3. Install requirements.
    ```
    python -m pip install -r requirements.txt
    ```
4. Setup environment variables. Get required access keys from [twitter developer](https://developer.twitter.com/en).
    ```
    export CONSUMER_KEY="hidden"
    export CONSUMER_SECRET="hidden"
    export ACCESS_TOKEN="hidden"
    export ACCESS_TOKEN_SECRET="hidden"
    ```
5. Run TweetListener.
    ```
    python TweetListener.py 
    ```
6. Run the iPython notebook `SentimentAnalysis.ipynb` for sentiment analysis.

# References

- https://realpython.com/twitter-bot-python-tweepy/
- https://towardsdatascience.com/sentiment-analysis-on-streaming-twitter-data-using-spark-structured-streaming-python-fc873684bfe3