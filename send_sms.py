# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
# Warning: you must replace the values below!
account_sid = "AC3b871b8dc7bb3785cddda6fd9ad271fe"  #WARNING: replace with your own account_sid
auth_token = "6b65df96c48e7d3b99ac574d872af60a"  #WARNING: replace with your own auth_token
tonumber = "+17816402658"  #WARNING: replace with your own cell phone numer
fromnumber = "+17815705388"  # WARNING: replace with your own TWILIO account number
body_text = "Sample text"  # replace with sample text for your message

print "Preparing to send text from %s to %s" % (fromnumber, tonumber)

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+17816402658", 
								 from_="+17815705388", 
								 body=body_text)

# media_links = ['https://upload.wikimedia.org/wikipedia/commons/5/55/Phillips_Academy_Andover_Coat_of_Arms.png', 'http://vignette1.wikia.nocookie.net/pokemon/images/f/fc/025Pikachu_OS_anime_5.png/revision/20150101093704']
# message = client.messages.create(to="+17816402658", 
# 								 from_="+17815705388", 
# 								 media_url=media_links)

print "Text successfully sent!"
