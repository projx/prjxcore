import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='prjxcore',
     version='0.34' ,
     author="prjx",
     author_email="kelvin@prjx.uk",
     description="A collection of base-classes used for common tasks, such as Config loading, logging etc",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3"
     ],
 )

