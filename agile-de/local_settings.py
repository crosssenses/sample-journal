import os, sys
sys.path.append(os.path.abspath("../../beautiful-reports/django"))
from settings.base import *

# Development Settings

DEBUG=True
SUPER_DEBUG=False

# Path settings

PROJECT_DIR = os.path.dirname(__file__)
PAGES_DIRECTORY = PROJECT_DIR
OUTPUT_DIRECTORY=os.path.join(BASE_DIR, "_build")

STATICFILES_DIRS = [
    STATIC_ROOT,
    os.path.join(PROJECT_DIR, "static"),
]
