from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,TWILIO_FROM_NUMBER,TWILIO_TO_NUMBER

# Config params
account_sid = TWILIO_ACCOUNT_SID
auth_token  = TWILIO_AUTH_TOKEN
toPhone = TWILIO_TO_NUMBER
fromPhone = TWILIO_FROM_NUMBER

# Set client
client = Client(account_sid, auth_token)

# New message
message = client.messages.create(
    to=  toPhone, 
    from_= fromPhone,
    body="Hello from Python!")

print(message.sid)
