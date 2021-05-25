import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user = api.me()
# print(user.screen_name)

### Dealing with tweeter request limiter 
def limit_handeler(cursor):
    '''
    Pauses the exceution of the requests to Twitter Servers to the RateLimitError
    '''
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

    

### Auto Follow back
def auto_follow_back():
    '''
    follows back any follower with more than 100 followers
    '''
    for follower in limit_handeler(tweepy.Cursor(api.followers).items()):
        if follower.followers_count > 100:
            follower.follow()

def narcissist_bot(search_string, numbersOfTweets):
    '''
    Search on main user time line for any tweet containig the key word: search_string and puts it in to favorites, also the number of times is limited by numbersOfTweets
    You can put your name as search_string to like any tweet containig your name
    '''
    for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
        try:
            tweet.favorite()
            print('Tweet Liked')
        except tweepy.TweepError as err:
            print(err.reason)
        except StopIteration:
            break

def retweet_bot(search_string, numbersOfTweets):
    '''
    Searchs on main user time line for any tweet containig the key word: search_string and retweets it in to favorites, also the number of times is limited by numbersOfTweets
    You can put your name as search_string to like any tweet containig your name
    '''
    for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
        try:
            tweet.retweet()
            print('Tweet Liked')
        except tweepy.TweepError as err:
            print(err.reason)
        except StopIteration:
            break



        
