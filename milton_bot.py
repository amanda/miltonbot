from twython import Twython
from pymarkovchain import MarkovChain
import string

APP_KEY = 'xuPB9BcyotCdrB5t13K8Q'
APP_SECRET = 'TtmtMcYrNGpi7fhgr8pDkmpPbUOy9xuhTVulbuM'
OAUTH_TOKEN = '2285416724-Bz9wfxHPDKFD15ewhirC39upOO9GN4fE8xzHYTM'
OAUTH_TOKEN_SECRET = 'gC2XSxvur8PfgkHi2C9kAkHQoffWvdMrcZ7l9KWUy4pxt'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

mc = MarkovChain("./markov")
mc.generateDatabase(open("./milton-paradise.txt").read())

def remove_punc(a_string):
	punc = tuple(string.punctuation)
	if a_string.endswith(punc):
		a_string = a_string[:-1]
	return a_string

def tweet():
    paradise_string = mc.generateString()
    remove_punc(paradise_string)
    twitter.update_status(status=paradise_string)

if __name__ == '__main__':
	tweet()