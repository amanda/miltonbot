from twython import Twython
from pymarkovchain import MarkovChain

APP_KEY = 'xuPB9BcyotCdrB5t13K8Q'
APP_SECRET = 'TtmtMcYrNGpi7fhgr8pDkmpPbUOy9xuhTVulbuM'
OAUTH_TOKEN = '2285416724-Bz9wfxHPDKFD15ewhirC39upOO9GN4fE8xzHYTM'
OAUTH_TOKEN_SECRET = 'gC2XSxvur8PfgkHi2C9kAkHQoffWvdMrcZ7l9KWUy4pxt'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

mc = MarkovChain("./markov")
mc.generateDatabase(open("./milton-paradise.txt").read())

def tweet():
    paradiseString = mc.generateString()
    twitter.update_status(status=paradiseString)

tweet()