import text2speech

speech_voice = 'en-AU-Catherine'
azureSpeechServiceKey = '2f57f2d9f1074faaa0e9484e1f1c08c1'

tts = text2speech.TextToSpeech(azureSpeechServiceKey, enableMemCache=False, enableDiskCache=False, voice=speech_voice)

tts.play("hello world")