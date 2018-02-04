import tweepy,json,time,sys


with open('twitter_auth.json') as file:
    secrets = json.load(file)
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'ilIlU0oxWV5RU4UEMxJgbxpmu'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'NHSAWA2sbzNoIvoKpd1wLwD2AfQNVBAdQe5U6s6ogXmxWhWTTs'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '959917752164278272-DaoRvj0fUoa0ckkdPu8wzS5A9GS1iPU'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'PygrfmtFUEqfpwmV5l86BEZ92DmF06NLIhRSEzZflqud5'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_with_media('male.png', 'This is a test')
