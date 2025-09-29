from task_manager.crud.models.base import db,engine
from task_manager.crud.models.user import User
from task_manager.crud.models.task import Task


db.metadata.create_all(engine)
print('Tables created sucessfully')