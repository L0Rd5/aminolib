from setuptools import setup, find_packages
with open("README.md", "r") as stream:
    long_description = stream.read()
setup(name="aminolib",version="1.1.1",url=None,download_url=None,description="lib for amino",long_description=long_description,install_requires=["datetime","flask","requests","json-minify"],keywords=["amino","aminolib","Lord","AminoAPI"],python_requires=">=3.6")