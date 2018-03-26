import os, sys
sys.path.append(os.path.abspath("../../graphite"))
from local_django.settings.base import *

# Development Settings

DEBUG=True
SUPER_DEBUG=False

# Path settings

PROJECT_DIRECTORY = os.path.dirname(os.path.dirname(__file__))
PAGES_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "pages")
OUTPUT_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "_build")
STATIC_ROOT = os.path.join(PROJECT_DIRECTORY, "_build", "static")

#STATICFILES_DIRS = [
#    os.path.join(PROJECT_DIRECTORY, "static"),
#]

LOCAL_JINJA_PATH = os.path.join(
    os.path.dirname(PROJECT_DIRECTORY),
    "jinja2",
)

TEMPLATES[0]["DIRS"] = [LOCAL_JINJA_PATH, ] + TEMPLATES[0]["DIRS"]

# Domains

SHARE_DOMAIN = "http://idist.io/g/lrnlab-agile/"
SHARE_DOMAIN_FULL = "https://www.impactdistillery.com/graphite/lrnlab-agile-en/"
