import os, sys
from graphite_paper.local_django.settings.base import *

# Development Settings

DEBUG=True
SUPER_DEBUG=False

# Path settings

PROJECT_DIRECTORY = os.path.dirname(os.path.dirname(__file__))
PAGES_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "pages")
OUTPUT_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "_build")
STATIC_ROOT = os.path.join(PROJECT_DIRECTORY, "_build", "static")

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIRECTORY, "static"),
]

LOCAL_JINJA_PATH = os.path.join(
    os.path.dirname(PROJECT_DIRECTORY),
    "jinja2",
)

TEMPLATES[0]["DIRS"] = [LOCAL_JINJA_PATH, ] + TEMPLATES[0]["DIRS"]