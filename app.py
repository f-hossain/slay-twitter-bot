from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import random
import tweepy

app = Flask(__name__)

@app.route('/')
def tweet():
    tweetArr = [
        "what if i flop? oh but my darling what if you slay?", 
        "doubt exists only in the mind", 
        "fortune favours the bold", 
        "take it easy but take it nonetheless"
    ]

    # authenticate app + user
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication Successful")
    except:
        print("Authentication Error")


    # select a random quote to tweet
    tweet = random.choice(tweetArr)
    api.update_status(tweet)

    # get number of posts to represent number of days slaying
    user_id = 57741058 
    user = api.get_user(user_id)
    statuses_count = user.statuses_count

    return '<h1>{statuses_count} days of slaying and counting!</h1>'


sched = BackgroundScheduler()
sched.add_job(tweet, 'interval', minutes=1440)
sched.start()

if __name__=='__main__':
    app.run(debug=True)

