# en_audio2text

Small module build with the help of speech_recognition package
Can be used for getting english transcription from audio via microphone or audio file

The code is written in Python 3

Instuctions for installation using pip
------------
1) pip install SpeechRecognition PyAudio
2) pip install en-audio2text-soumyade 



  
Example 1: Using microphone
--------

.. code:: python

    from en_audio2text.aud2text import SpeechRecognizer
    
    sr = SpeechRecognizer()
    sr.act()
    
    
  Here is the sample ouput:
  
  Please wait while we transcribe...
  
  'hi I am Alexios of sparta one of the many invincible warrior in the army'


Example 2: Using audio file
--------

.. code:: python

    from en_audio2text.aud2text import SpeechRecognizer
    
    sr = SpeechRecognizer(src='file')
    sr.act('my_audio_file.wav')
    
    
  Here is the sample ouput:
  
  Please wait while we transcribe...
  
  'you can not change what you have done wrong intentionaly in the past'


Example 3: Display all possible transcription
--------

.. code:: python

    from en_audio2text.aud2text import SpeechRecognizer
    
    sr = SpeechRecognizer(debug=True)
    sr.act()
    
    
  Here is the sample ouput:
  
  Please wait while we transcribe...
  
  {'alternative': [{'transcript': 'hi I am Alexios Sparta one of the many invincible why you are in the army',
   'confidence': 0.79579026},
  {'transcript': 'hi I am Alexa Sparta one of the many invincible why are you in the army'},
  {'transcript': 'hi I am Alexis part one of the many invincible why you are in the army'},
  {'transcript': 'hi I am Alexis Hospital one of the many invincible why you are in the army'},
  {'transcript': 'hi I am Alexis part one of the many invincible why are you in the army'}],
 'final': True}