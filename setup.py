import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='akamaiproperty',
     version='2.0',
     author="Achuthananda M P",
     author_email="achuthadivine@gmail.com",
     description="A Pip Package for Akamai Property",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Achuthananda/AkamaiProperty",
     packages=['akamaiproperty'],
     install_requires=['edgegrid-python','requests'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
