"Dad jokes in Python"

from __future__ import absolute_import
import pandas as pd
from .dad_jokes import get_joke

__project__ = "test-github-actions-jg"
__version__ = "develop"
__keywords__ = ["jokes", "joke", "dadjokes"]
__author__ = "Jarred Glaser"
__author_email__ = "jarred.glaser@gmail.com"
__url__ = "https://www.jarredglaser.com/"
__platforms__ = "ALL"

__classifiers__ = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License'
]

__requires__ = ["pandas"]

__extra_requires__ = {
}
