import os
from logging import DEBUG


API_USER_NAME = 'user'
API_USER_PASS = 'pass'

LOG_LEVEL = DEBUG

NOTIF_URL = 'https://2055430c-dd72-485c-a364-74be856d1875.mock.pstmn.io/send-notification'

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
