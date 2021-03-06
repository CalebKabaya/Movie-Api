from app import create_app
from app import db
from flask_script import Manager,Server
from app.models import User,Role,Review
from flask_migrate import Migrate,MigrateCommand


# Creating app instance
# app = create_app('development')
# # app = create_app('test')
app = create_app('production')



manager = Manager(app)
manager.add_command('server',Server)

manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_contex():
    return dict(app =app,db=db,User=User, Role=Role)
if __name__ == '__main__':
    manager.run()