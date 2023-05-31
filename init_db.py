from app import models, database

from app import User, Item

models.Base.metadata.create_all(bind=database.engine)
