import os, sys
sys.path.append(os.path.abspath("../../graphite"))
from local_django.settings.base import *

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

LOCAL_JINJA_PATH = os.path.join(
    os.path.dirname(PROJECT_DIRECTORY),
    "jinja2",
)

TEMPLATES[0]["DIRS"] = [LOCAL_JINJA_PATH, ] + TEMPLATES[0]["DIRS"]

