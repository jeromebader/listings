import os


class Config(object):
    SECRET_KEY = os.urandom(12)




class Emailserver(object):
    MAIL_SERVER = 'mail.mailserver.cl'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'confirmation@mailserver.cl'
    MAIL_DEFAULT_SENDER = 'confirmation@mailserver.cl'
    MAIL_PASSWORD = 'password'

# administrator list
    ADMINS = ['confirmation@mail.cl']