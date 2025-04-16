import tweepy
import requests
from bs4 import BeautifulSoup

# Twitter API credentials (replace with your own)
API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ' '
ACCESS_TOKEN_SECRET = ''

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key=API_KEY,
                                consumer_secret=API_SECRET_KEY,
                                access_token=ACCESS_TOKEN,
                                access_token_secret=ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Function to scrape the daily quote from BrainyQuote
def get_daily_quote():
    url = 'https://www.brainyquote.com/quote_of_the_day'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # The quote is inside a div with the class 'qotd-qc'
    quote = soup.find('div', class_='qotd-qc').find('a').text.strip()
    
    return quote

# Function to post the daily tweet
def post_tweet():
    try:
        quote = get_daily_quote()  # Scrape the quote of the day
        api.update_status(quote)  # Post the quote to Twitter
        print("Successfully posted tweet: ", quote)
    except Exception as e:
        print("Error while posting tweet:", e)

# Call the function to post the tweet every time the script is launched
post_tweet()
