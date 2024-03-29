from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

env_name = 'development'
app = app(env_name)
migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
