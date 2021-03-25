[metadata]
# replace with your username:
name = en_audio2text-soumyade
version = 1.0.1
author = Soumya De
author_email = cs.soumyade@gmail.com
description = small wrapper around speech recognition package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/cssoumyade/en_audio2text
project_urls =
    Bug Tracker = https://github.com/cssoumyade/en_audio2text/issues
install_requires = 
	speech_recognition
	pyaudio
classifiers =
        Development Status :: 2 - Pre-Alpha
        Intended Audience :: Other Audience
        Topic :: Education :: Testing
        License :: OSI Approved :: MIT License
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.6

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src




import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="en_audio2text-soumyade", # Replace with your own username
    version="1.0.2",
    author="Soumya De",
    author_email="cs.soumyade@gmail.com",
    description="small wrapper around speech recognition package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cssoumyade/en_audio2text",
    project_urls={
        "Bug Tracker": "https://github.com/cssoumyade/en_audio2text/issues",
    },
    install_requires=[ 
	speech_recognition,
	pyaudio]
    classifiers=[
	"Development Status :: 2 - Pre-Alpha"
	"Intended Audience :: Other Audience"
	"Topic :: Education :: Testing"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
