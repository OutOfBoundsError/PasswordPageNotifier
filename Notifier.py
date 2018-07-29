import requests
from discord_hooks import Webhook
from twilio.rest import TwilioRestClient
import time

# SET YOUR TWILIO PHONE NUMBER. GET ONE AT https://www.twilio.com/try-twilio
# Format it with +1#######
TWILIO_PHONE_NUMBER = "+1"

#Set your phone number
# Format it with +1######
Target_number = "+1" 

TWIML_INSTRUCTIONS_URL = \
"http://static.fullstackpython.com/phone-calls-python.xml"

# First param is your account SID, Second Param is your AUTH Code. You can find those at https://www.twilio.com/console
client = TwilioRestClient("AC######", "######") # First param is your account SID, Second Param is your AUTH Code. You can find those at

#Set to your Discord Webhook url
webHookUrl = 'https://discordapp.com/api/webhooks/######'
embed = Webhook(webHookUrl, color=123123)

def call(target):
    print("Calling " + target)
    client.calls.create(to=target,from_=TWILIO_PHONE_NUMBER,url = TWIML_INSTRUCTIONS_URL, method="GET")

def sendMessage(bot):
    bot.set_author(name='Password Monitor')
    bot.set_desc('ToyTokyo is Live!!!!')
    #Set value below to the link of your desired page without password
    #Example: if your desired page is https://yeezysupply.com/password then you would enter https://yeezysupply.com
    bot.add_field(name='Link: ', value='https://launch.toytokyo.com')
    bot.set_footer(ts=True)
    bot.post()

req = requests.Session()
req.headers.update({
    'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
})

isPassword = True
#Tests for discord webhook and phone number.
#call(Target_number)
#sendMessage(embed)

while (isPassword):
    response = req.get('https://launch.toytokyo.com/')
    if ('password' in response.url):
        print('Not Live')
        print (response.url)
        time.sleep(5) #Refresh delay
    else:
        call(Target_number)
        sendMessage(embed)
        print('Live')
        isPassword = False

    
