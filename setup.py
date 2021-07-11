import setuptools
import os


PACKAGE_NAME = 'akamaiproperty'
PACKAGE_KEYWORDS = [
    'Akamai',
    'Property',
    'CDN',
    'AkamaiConfigs',
    'Edge',
]

project_root = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the project's README.rst file
with open(os.path.join(project_root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
     name=PACKAGE_NAME,
     version='2.1',
     author="Achuthananda M P",
     author_email="achuthadivine@gmail.com",
     description="A Pip Package for Akamai Property",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Achuthananda/AkamaiPropertyManager",
     packages=['akamaiproperty'],
     install_requires=['edgegrid-python','requests'],
     keywords=" ".join(PACKAGE_KEYWORDS),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
