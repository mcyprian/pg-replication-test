import os

from sqlalchemy import create_engine


def db_engine():
    params = {
        "host": os.environ["DATABASE_SERVICE_NAME"],
        "database": os.environ["DATABASE_NAME"],
        "user": os.environ["DATABASE_USER"],
        "password": os.environ["DATABASE_PASSWORD"],
    }
    return create_engine(
        "postgresql://{user}:{password}@{host}/{database}".format(**params)
    )
