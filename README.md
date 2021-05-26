# Twitter_bot_python

A python Bot using **tweepy** library.

## Description:

It's a simple way to connect your user account to the script so you can automate functions as retweet, follow back or put on favorites

## Configuration:

You need to replace this two lines providing your own API key from the developer console on Twitter, it is 100% necessary to connect the script to you user account

**More info on:**

[twitter API](https://developer.twitter.com/en/docs/twitter-api)

```python

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

```

## Usage

The script has ****3**** basic functions ready to usage.

- **auto_follow_back(followers_count):** follows back any follower with more than followers_count input parameter.
- **narcissist_bot(search_string, numbersOfTweets):** Search on main user time line for any tweet containing the key word: search_string and puts it in to favorites, also the number of items is limited by numbersOfTweets
You can put your name as search_string to like any tweet containig your name.

- **retweet_bot(search_string, numbersOfTweets):** Search on main user time line for any tweet containing the key word: search_string and retweets it in to favorites, also the number of items is limited by numbersOfTweets
You can put your name as search_string to retweet any tweet containig your name

### Other usage

As the script uses the ****tweepy**** library you can easily create your own functions in order to fulfill your needs.

You can read more info on:

[TweePy Documentation](https://docs.tweepy.org/en/latest/)

## Final Note

This script could be possible thanks to ZTM Python development Course by Andrei Neagoie.
