import setuptools
  
# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()
    
    
# specify requirements of your package here
REQUIREMENTS = ['SpeechRecognition', 'pyaudio']

# some more details
classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Other Audience",
        "Topic :: Education :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ]


# calling the setup function 
setup(name='en_aud2text',
      version='1.0',
      description='small wrapper around speech recognition package',
      long_description=long_description,
      url='https://github.com/cssoumyade/en_audio2text',
      author='Soumya De',
      author_email='cs.soumyade@gmail.com',
      license='MIT',
      package_dir={"": "en_audio2text"},
      packages=setuptools.find_packages(where="en_audio2text"),
      classifiers=classifiers,
      install_requires=REQUIREMENTS,
      keywords='speech audio text transcription'
      )

