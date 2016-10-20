import tweepy
from tweepy import OAuthHandler
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
 
consumer_key = 'uGR6NQOLUIXmzSSuJFSFhbY3i'
consumer_secret = 'AeRZnA0ziRlNYSSQIjLyh84uObw9b2iiTghDPZukIwhjwsbH1H'
access_token = '84530015-pBpdPD8QCsJksYTosHvIjicAtAC8t8FhVdxGreCt7'
access_secret = 'JGZ4KNFiqPtYm1E5wAlXLMhzpqtA49Dk4ucXeYZ256PT5'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))
    

 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('FirstDayofFall.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status
    
if __name__ == '__main__':


# https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/        
#     twitter_stream = Stream(auth, MyListener())
#     twitter_stream.filter(track=['#FirstDayofFall'])


# http://code.runnable.com/Us9rrMiTWf9bAAW3/how-to-stream-data-from-twitter-with-tweepy-for-python
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    print "Showing all new tweets for #FirstDayofFall:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['FirstDayofFall'])

