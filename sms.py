from twilio.rest import Client
account_sid="AC22db9641789ab2fef40ae5accdedcb58"
auth_token="6dcda19dee9cbd30c733352834d28b9d"
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="this message is coming from my nyaanga beast python script",
                     from_='+15592060953',
                     to='+254708701061'
                 )

print(message.sid)