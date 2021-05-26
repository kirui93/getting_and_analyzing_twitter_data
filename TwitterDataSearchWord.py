# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:31:59 2021

@author: Kipngeno Kirui @ 2021
"""

__author__ = "Kipngeno Kirui <kipngenokirui1993@gmail.com>"


"""
In the following, we are going to write a function that employs Tweepy package
and extract tweets from Twitter using a particular search word or hashtag.

To do this, you need to create a developer account in Twitter and register
an app to get your Twitter credentials. These credentials are:
    1. Consumer Key
    2. Consumer secret
    3. Access token
    4. Access token secret.

We will write a try-and-except function to check if these credentials are OKAY.

There are a lot of information we can access in Twitter, some are from personal account and 
some describe the tweet. We will access this information about a particular hashtag and save
them to a CSV file for further analysis.

Saving them to a CSV file helps us to generate a Pandas dataframe later for easier data analysis in Python.
"""

#import sys
import csv   # we need this to write and tweets to a CSV file.
from datetime import date # we need this to set up dates.
import tweepy  #http://www.tweepy.org/

# Get your Twitter API credentials and enter them here
# Set up credentials
consumer_key = "YOUR CODE HERE"
consumer_secret = "YOUR CODE HERE"
access_token = "YOUR CODE HERE"
access_token_secret = "YOUR CODE HERE"
bearer_token = "YOUR CODE HERE"

# Set up the search word
search_word = "BBI"


def get_tweets_search_word(search_word):
    # set up your authentication from tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True)
    
    # Check the credentials if they are okay.
    try:
        api.verify_credentials()
        print("Your API Credentials are OKAY!")
    except:
        print("Error during authentication")
           
    # Set up some search paramaters
    # 1. Number of tweets to be collected
    # 2. The start date
    # 3. The last date (today)
    # 4. An empty array to collect the tweets
    
    number_of_tweets = 10000
    since_date = date(2020, 1, 1)
    until_date = date.today()
    tweets_for_csv = []
    
    ## To search tweets restricted to a certain place/country, uncomment the following 2 lines
    
    #places = api.geo_search(query = "Kenya", granularity="country")
    #place_id = places[0].id
    
    # Change the "q" in the FOR loop to the following so as to restrict to your place/country.
    
    # q='{} place:{}'.format(search_word, place_id)  # restricting the search to a certain place

    for tweet in tweepy.Cursor(api.search, 
                               q = search_word, 
                               since = since_date, 
                               until = until_date, 
                               tweet_mode="extended",
                               lang = "en").items(number_of_tweets):
        # We want to collect tweets from the original source.
        # Therefore we will include an IF condition to restrict collecting retweets
        # and also tweets with no likes.
        #if (not tweet.retweeted) and ('RT @' not in tweet.text) and (tweet.favorite_count > 0):
            # Append tweets to the list with the following information:
            # 1. When the tweet was created
            # 2. The name of person owning the account
            # 3. The username in the account
            # 4. Whether the account is verified
            # 5. The location of the person when he/she/it tweeted
            # 6. The number of users currently following this account
            # 7. The number of users the account is currently following
            # 8. When the account was created.
            # 9. Tweet text
            # 10. The number of likes of the tweet
            # 11. The number of retweets of the tweet
            # 12. The device used posting the tweet.
            # 13. Whether the tweet is a quote.
        tweets_for_csv.append([tweet.created_at, tweet.user.name, tweet.user.screen_name, 
                               tweet.user.verified, tweet.user.location, 
                               tweet.user.followers_count, tweet.user.friends_count, tweet.user.created_at,
                               tweet.full_text, tweet.favorite_count, tweet.retweet_count,
                               tweet.source, tweet.is_quote_status])
        
    
    # write the array of tweets to a new CSV file.
    outfile = search_word + "_tweets.csv"
    print("writing to " + outfile)
    # Include "newline = '' " to prevent writing empty lines after even row.
    # Write the row header before writing the rows of tweets.
    with open(outfile, 'w+', encoding = "utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["created_at", "full_name", "username", "verified", "location", 
                         "followersCount", "friendsCount", "accountCreatedAt", 
                         "tweet", "likes", "retweets", "device", "isquote"])
        writer.writerows(tweets_for_csv)
        
#if we're running this as a script
if __name__ == '__main__':
    get_tweets_search_word(search_word)
    
    # If you have many search words and you would like to find tweets for all once,
    # then you can do it in a FOR loop as follows.
    
    # Tweets for each of the search word will be saved to a CSV file respectively.
    
    #search_words = ["BBI", "constitution", "elections", "wanjiku", "#LFC"]
    #for sw in search_words:
        #get_tweets_search_word(sw)