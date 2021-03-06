from db_config import SQLALCHEMY_DATABASE_URI, FACEBOOK_APP_ID, FACEBOOK_APP_SECRET

def randomkey(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


SQLALCHEMY_POOL_RECYCLE = 3600
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = randomkey(30)
DEBUG = True

