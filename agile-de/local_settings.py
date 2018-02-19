import os, sys
sys.path.append(os.path.abspath("../../beautiful-reports/django"))
from settings.base import *

# Development Settings

DEBUG=True
SUPER_DEBUG=False

# Path settings

PROJECT_DIRECTORY = os.path.dirname(__file__)
PAGES_DIRECTORY = PROJECT_DIRECTORY

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIRECTORY, "static"),
]
