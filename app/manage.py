from flask_script import Manager
from flask_ci import CICommand

from app import app
from tests import settings

manager = Manager(app)
manager.add_command('ci', CICommand(settings))

if __name__ == "__main__":
    manager.run()