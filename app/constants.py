"""App wide Constants"""

import datetime
from os import path

YEAR = (datetime.date.today()).year
STRING_YEAR = str(YEAR)
BASE_DIR = path.abspath(path.dirname(__file__))