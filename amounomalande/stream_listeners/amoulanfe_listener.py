from tweepy import StreamListener


class AmoulanfeListener(StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, status):
        try:
            status.retweet()
        except:
            pass
