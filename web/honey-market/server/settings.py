import os
import random

def random_password(length=30):
    # Simply just a functiton generating random password, nothing big of a deal
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+-=`;:\'"\\,<.>/?'
    return ''.join(random.choices(alphabets, k=length))

BLIST = open("/tmp/black_list_ip_later.txt", "w+")
def black_list_later(ip):
    BLIST.write(ip+"\n")
    BLIST.flush()

environments = os.environ

SECRET_KEY = environments["SECRET_KEY"] if 'SECRET_KEY' in environments else random_password(1000)

PORT = environments["PORT"] if 'PORT' in environments else 5000

HOST = environments["HOST"] if 'HOST' in environments else "127.0.0.1"

SQLALCHEMY_DATABASE_URI = environments["SQLURI"] if 'SQLURI' in environments else "sqlite:///dev.db"

# Development state
DEVELOPMENT = False if 'PRODUCTION' in environments else True 

# Administrator settings
ADMIN_USERNAME = environments["ADMIN_USERNAME"] if 'ADMIN_USERNAME' in environments else "Administrator"
ADMIN_PASSWORD = environments["ADMIN_PASSWORD"] if 'ADMIN_PASSWORD' in environments else random_password()
# print("Admin password is: ", ADMIN_PASSWORD)

# Extra environment variables
MOTD_QUOTE = environments["MOTD"] if 'MOTD' in environments else "REDACTED_MOTD"
CAN_BE_FLAG = environments["FLAG"] if 'FLAG' in environments else "REDACTED_FLAG"

# Profile image directory
CURRENT_DIR = os.path.dirname(__file__)
PROFILE_IMAGE_DIR = os.path.join(CURRENT_DIR, "profile_images")
DATABASE_DIR = os.path.join(CURRENT_DIR, "instance")
DATABASE_FILE = os.path.join(CURRENT_DIR, "instance", "dev.db")