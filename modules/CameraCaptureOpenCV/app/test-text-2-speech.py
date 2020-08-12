import text2speech

speech_voice = 'en-AU-Catherine'
azureSpeechServiceKey = ''

tts = text2speech.TextToSpeech(azureSpeechServiceKey, enableMemCache=False, enableDiskCache=False, voice=speech_voice)

tts.play("hello world")