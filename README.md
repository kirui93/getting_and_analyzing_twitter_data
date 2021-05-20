# Twitter Data

This repository contains a Python script that I used in getting data from Twitter API.

The script basically requires you to have Twitter cridentials and a search word for you to obtain tweets and save it to a CSV file for further analysis.

The credentials required are:

    1. Consumer Key
    2. Consumer secret
    3. Access token
    4. Access token secret.

Search word can be any word or an hashtag that you want to analyze in Python.

## Required packages

For you to use this script, you need the following Python packages:

    1. Pandas
    2. Tweepy
    3. CSV
    4. Datetime
 
## Tweet characteristics

For each tweet that we pull from Twitter, the following are the information that we capture:

    1. When the tweet was created
    2. The name of person owning the account
    3. The username in the account
    4. Whether the account is verified
    5. The location of the person when he/she/it tweeted
    6. The number of users currently following this account
    7. The number of users the account is currently following
    8. When the account was created.
    9. Tweet text (what the tweet contains)
    10. The number of likes of the tweet
    11. The number of retweets of the tweet
    12. The device used posting the tweet.
    13. Whether the tweet is a quote.
    
These are what will be our columns in the CSV file that we are creating.


## Final remarks

Pass through the script and in case of any *questions*, *comments* or *additions*, please feel free to open a **GitHub issue** and I will do the necessary.

I am going to write a LinkedIn blog for analysis of **_BBI_** tweets and post the link here when I am done.

Happy coding!
