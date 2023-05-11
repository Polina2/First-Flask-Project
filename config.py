class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:' + open("secrets.txt", 'r').read() + '@localhost:5432/tel_app'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
