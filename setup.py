import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi (if you dont need delete it)
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# you need to change all these
VERSION = '1.5.1'
DESCRIPTION = 'an enhanced version of the print function'

setup(
    name="colorful_prints",
    version=VERSION,
    author="hxy",
    author_email="hxy2321548628@163.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['rich'],
    keywords=['python', 'print', 'color','red','green','yellow'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url="https://github.com/hxy2321548628/color_prints",  
    license="MIT",  
)
