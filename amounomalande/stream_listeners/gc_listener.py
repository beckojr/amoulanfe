from tweepy import StreamListener
import re


class GCListener(StreamListener):
    def __init__(self, api, response):
        self.api = api
        self.me = api.me()
        self.response = response

    def on_status(self, status):
        print("New status event")
        if (
            status.in_reply_to_status_id is None
            and status.is_quote_status == False
            and not hasattr(status, "retweeted_status")
        ):
            m = re.compile("guin[eé][ea][- ]conakry", re.IGNORECASE)
            status_text = (
                status.extended_status["full_text"] if status.truncated else status.text
            )
            if m.search(status_text) is not None:
                print("Match found")
                self.api.update_status(
                    self.response.format(mention=status.user.screen_name),
                    in_reply_to_status_id=status.id,
                    auto_populate_reply_metadata=True,
                )
                print("Replied to")
