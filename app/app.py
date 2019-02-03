from flask import Flask
from flask_script import Manager
from flask_ci import CICommand
from tests import settings
import time
app = Flask(__name__)

# import pit.liveStream
#import pit.matchData
#import pit.matchSchedule
# import scouting.templatingData

import scouting.data as data
import scouting.matchScouting as matchScouting
import scouting.pitScouting as pitScouting
SCOUTING_PREFIX = '/scouting'

app.register_blueprint(data.bp, url_prefix = '/scouting')
app.register_blueprint(matchScouting.bp, url_prefix = '/scouting')
app.register_blueprint(pitScouting.bp, url_prefix = '/scouting')



import publicity.publicityBoard as publicityBoard

app.register_blueprint(publicityBoard.bp)

manager = Manager(app)
manager.add_command('ci', CICommand(settings))

if __name__ == "__main__":
    manager.run()