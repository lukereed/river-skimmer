"""
Configuration
"""

import os
from dotenv import find_dotenv, load_dotenv

find_dotenv()
load_dotenv()


RECREATION_API_BASE_URL = 'https://www.recreation.gov/api/'

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

SMTP_EMAIL_ADDRESS = os.getenv("SMTP_EMAIL_ADDRESS")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_SERVER=os.getenv("SMTP_SERVER")
