from flask import Flask
from flask_script import Manager
from flask_ci import CICommand
from tests import settings
import time
app = Flask(__name__)


import __init__
# import pit.liveStream
#import pit.matchData
#import pit.matchSchedule
#import publicity.publicity
from scouting.matchScouting import matchScouting
# import scouting.pitScouting
# import scouting.templatingData

from scouting.data import bp

app.register_blueprint(bp)
app.register_blueprint(matchScouting)

manager = Manager(app)
manager.add_command('ci', CICommand(settings))

if __name__ == "__main__":
    manager.run()

app.run(port=5001)