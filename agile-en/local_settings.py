import os, sys
sys.path.append(os.path.abspath("../../graphite/graphite"))
from settings.base import *

# Development Settings

DEBUG=True
SUPER_DEBUG=False

# Path settings

PROJECT_DIRECTORY = os.path.dirname(__file__)
PAGES_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "pages")
STATIC_ROOT = os.path.join(BASE_DIR, "report", "static")

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIRECTORY, "static"),
]

TEMPLATES[0]["DIRS"].append(os.path.join(
    os.path.dirname(PROJECT_DIRECTORY),
    "jinja2",
))
