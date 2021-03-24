from setuptools import setup
  
# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()
    
    
# specify requirements of your package here
REQUIREMENTS = ['SpeechRecognition', 'pyaudio', 'regex', 'os-sys']

# some more details
classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ]


# calling the setup function 
setup(name='en_aud2text',
      version='0.0.1',
      description='small wrapper around speech recognition package',
      long_description=long_description,
      url='https://github.com/cssoumyade/en_audio2text',
      author='Soumya De',
      author_email='cs.soumyade@gmail.com',
      license='MIT',
      packages=['en_audio2text'],
      classifiers=classifiers,
      install_requires=REQUIREMENTS,
      keywords='speech audio text transcription'
      )

