import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7465878a1299fd185ce1f77c1ef6364d'