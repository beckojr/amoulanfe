from tweepy import OAuthHandler, API, Stream
from os import getenv
from stream_listeners import AmoulanfeListener, GCListener

auth = OAuthHandler(getenv("CONSUMER_API_KEY"), getenv("CONSUMER_API_SECRET_KEY"))
auth.set_access_token(getenv("ACCESS_TOKEN"), getenv("ACCESS_TOKEN_SECRET"))
api = API(auth)

# res_stream = open("response.txt", "r")
# res = res_stream.read()
# res_stream.close()

listener = AmoulanfeListener(api)
stream = Stream(auth=api.auth, listener=listener)

# gc_listener = GCListener(api, res)
# gc_stream = Stream(auth=api.auth, listener=gc_listener)

# gc_stream.filter(
#     track=["Guinee Conakry", "Guinée Conakry", "Guinée-Conakry", "Guinea Conakry"],
#     is_async=True,
# )

stream.filter(
    track=[
        "#Amoulanfe",
        "#FreeFonike",
        "#FNDC",
        "Guinee",
        "#AllRising4Guinea",
        "#Kibaro",
    ],
)
