import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='logmine',
     version='0.4.1',
     scripts=['logmine'],
     author="Tony Dinh",
     author_email="pip@tonydinh.com",
     description="Log pattern analyzer",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/trungdq88/logmine",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
