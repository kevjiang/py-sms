from flask import Flask, request, redirect
import twilio.twiml
import os
from handler import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def receive_sms():
    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    body = body.lower().strip()  # removes spaces and converts all to lower case

    message = response_handler(body)
 
    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.  For Heroku deployment
	# http://stackoverflow.com/questions/17260338/deploying-flask-with-heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)