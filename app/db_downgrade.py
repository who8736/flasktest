from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO
from config import SQLALCHEMY_DATABASE_URI

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

print('Current database version: ' + str(v))
