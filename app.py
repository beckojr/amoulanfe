import tweepy
import os

import logging

logger = logging.getLogger()


class AmoulanfeListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, status: tweepy.Status):
        logger.info("New status received")
        try:
            status.retweet()
        except:
            print("Already retweeted")


if __name__ == "__main__":
    auth = tweepy.OAuthHandler(
        os.getenv("CONSUMER_API_KEY"), os.getenv("CONSUMER_API_SECRET_KEY")
    )
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    api = tweepy.API(auth)
    listener = AmoulanfeListener(api)
    stream = tweepy.Stream(auth=api.auth, listener=listener)

    stream.filter(
        track=[
            "#Amoulanfé",
            "#Amoulanfe",
            "#Kibaro",
            "#Amoufuckinglanfe",
            "#Amoufuckinglanfé",
            "#FNDC",
        ]
    )
