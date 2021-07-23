url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/c6f0cb35-e9d0-4ec5-8332-2febd96c3070"
apikey = "luy7gQqCcyqxrFQLYRg9wf92_3YnevzfNKJ8eCi-bBiA"

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('testing', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)