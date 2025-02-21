import os
from dotenv import load_dotenv

load_dotenv()


SMTP_SERVER = os.environ['SMTP_SERVER']
SMTP_PORT = int(os.environ['SMTP_PORT'])
SMTP_EMAIL_ADDRESS = os.environ['SMTP_EMAIL_ADDRESS']
SMTP_PASSWORD = os.environ['SMTP_PASSWORD']

RECREATION_API_KEY = os.environ.get('RECREATION_KEY')
RECREATION_API_BASE_URL = 'https://www.recreation.gov/api/'
