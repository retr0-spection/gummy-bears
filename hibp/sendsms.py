from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def SMS(words):
    message = client.messages.create(body = words,
                                    from_='twillio number',
                                    to='your personal number')

    message.sid


