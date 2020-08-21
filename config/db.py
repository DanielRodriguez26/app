import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

MYSQL = {
  'default' : {
    'ENGINE' : 'django.db.backends.mysql',
    'OPTIONS': {
      'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
    'NAME' : 'db',
    'USER': 'root',
    'PASSWORD' : '',
    'HOST' : 'localhost',
    'PORT' : '3306'
  }
}