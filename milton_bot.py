from twython import Twython
from pymarkovchain import MarkovChain
import string

APP_KEY = 'blah'
APP_SECRET = 'blah'
OAUTH_TOKEN = 'blah'
OAUTH_TOKEN_SECRET = 'blah'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

mc = MarkovChain("./markov")
mc.generateDatabase(open("./milton-paradise.txt").read())

def remove_punc(a_string):
	punc = tuple(string.punctuation)
	if a_string.endswith(punc):
		a_string = a_string[:-1].strip()
	return a_string

def tweet():
    paradise_string = remove_punc(mc.generateString())
    twitter.update_status(status=paradise_string)

if __name__ == '__main__':
	tweet()