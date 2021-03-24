from setuptools import setup
  
# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()
    
    
# specify requirements of your package here
REQUIREMENTS = ['SpeechRecognition', 'pyaudio', 'regex', 'os-sys']

# some more details
CLASSIFIERS = [
    'Development Status :: Inception Phase - Beta 1.0',
    'Intended Audience :: Personal Use',
    'Topic :: Speech Recognition',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    ]


# calling the setup function 
setup(name='aud2text',
      version='0.0.1',
      description='small wrapper around speech recognition package',
      long_description=long_description,
      url='',
      author='Soumya De',
      author_email='cs.soumyade@gmail.com',
      license='MIT',
      packages=['en_audio2text'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='speech audio text transcription'
      )

