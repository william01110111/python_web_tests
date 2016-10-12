#!/usr/bin/python2

import httplib2
import urllib
import json
from twilio.rest import TwilioRestClient

# https://www.googleapis.com/language/translate/v2?key=YOUR_API_KEY&q=hello%20world&source=en&target=de

baseUrl = "https://www.googleapis.com/language/translate/v2"
apiKey = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"

def constructURL(text, targetLang):
	text = urllib.quote(text)
	return baseURL + "?" + "key=" + apiKey + "&" + "q=" + text + "&" + "target=" + targetLang

def getTranslation(text, targetLang):
	print("making http request...")
	response, body = httplib2.Http().request(constructURL(text, targetLang), method="GET")
	bodyDict = json.loads(body)
	translation = bodyDict["data"]["translations"][0]["translatedText"]
	return translation

def getTranslationArray(textLines, targetLang):
	out = []
	for text in textLines:
		translation = getTranslation(text, targetLang)
		translation = translation.encode('utf-8')
		out.append(translation)

	return out

#english = ["this is the first line", "this is the second line", "this is the third line"]
#spanish=getTranslationArray(english, "es")

#print(spanish)

#for i in spanish:
# 	print i

account_sid = "AC87769992cf0edbd7bfbd177e6c15a760"
auth_token = "5995687694981b0d7f5097a5ce418acb"

translation=getTranslation("hello, this is a test of my translate API wrapper", "es")
print(translation)

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to = "+12067084245",
    from_= "+12062072038",
    body = translation)
