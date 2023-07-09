DEBUG = True

USERNAME = "root"
PASSWORD = "Everton_12"
SERVER = "localhost"
DB = "sociovasco"

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True