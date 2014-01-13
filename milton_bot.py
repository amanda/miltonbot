from twython import Twython
from pymarkovchain import MarkovChain

APP_KEY = 'blah'
APP_SECRET = 'blah'
OAUTH_TOKEN = 'blah'
OAUTH_TOKEN_SECRET = 'blah'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

mc = MarkovChain("./markov")
mc.generateDatabase(open("./milton-paradise.txt").read())
paradiseString = mc.generateString()

twitter.update_status(status=paradiseString)