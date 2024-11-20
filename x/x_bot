import tweepy

API_KEY = "your_twitter_api_key"
API_SECRET = "your_twitter_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

def post_to_twitter(message):
    """
    Posts a message to Twitter.
    """
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )
    response = client.create_tweet(text=message)
    print(f"Tweet posted: {response.data['id']}")

if __name__ == "__main__":
    test_message = "Aura AI: Translating trading vibes into insights 🌐"
    post_to_twitter(test_message)
