import time,json,tweepy
from datetime import datetime

from time import sleep
from smtplib import SMTP
from smtplib import SMTPException
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



f_time = datetime.now().strftime('%a %d %b @ %H:%M')

with open('pictureTaken.json') as file:
    data = json.load(file)
toaddr = data['email']    # redacted
me = 'pictourmail@gmail.com' # redacted
subject = 'Photo ' + f_time

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = me
msg['To'] = toaddr
msg.preamble = "Here's your pic!\n\nCheck out the HQ version here!"

msgText = "Here's your pic!\n\nCheck out the HQ version here!"
body = MIMEText(msgText, 'plain')
msg.attach(body)

fp = open('photo.jpg', 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

with open('twitter_auth.json') as file:
	secrets = json.load(file)

CONSUMER_KEY = 'ilIlU0oxWV5RU4UEMxJgbxpmu'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'NHSAWA2sbzNoIvoKpd1wLwD2AfQNVBAdQe5U6s6ogXmxWhWTTs'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '959917752164278272-DaoRvj0fUoa0ckkdPu8wzS5A9GS1iPU'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'PygrfmtFUEqfpwmV5l86BEZ92DmF06NLIhRSEzZflqud5'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_with_media('photo.jpg', 'Pitastic!')


try:


   s = smtplib.SMTP('smtp.gmail.com',587)
   s.ehlo()
   s.starttls()
   s.ehlo()
   s.login(user = 'pictourmail@gmail.com',password = 'hackathon18')
   #s.send_message(msg)
   s.sendmail(me, toaddr, msg.as_string())
   s.quit()
#except:
#   print ("Error: unable to send email")
except SMTPException as error:
      print ("Error: unable to send email : ")