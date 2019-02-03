from flask import Flask
from flask_script import Manager, Server
from flask_ci import CICommand
from tests import settings

app = Flask(__name__)

app.debug = True

import pit.liveStream as liveStream
import pit.matchData as matchData
import pit.matchSchedule as matchSchedule
import pit.batteryTracker as batteryTracker
PIT_PREFIX = '/pit'

app.register_blueprint(liveStream.bp, url_prefix = PIT_PREFIX)
app.register_blueprint(matchData.bp, url_prefix = PIT_PREFIX)
app.register_blueprint(matchSchedule.bp, url_prefix = PIT_PREFIX)
app.register_blueprint(batteryTracker.bp, url_prefix = PIT_PREFIX)

import scouting.data as data
import scouting.matchScouting as matchScouting
import scouting.pitScouting as pitScouting
SCOUTING_PREFIX = '/scouting'

app.register_blueprint(data.bp, url_prefix = SCOUTING_PREFIX)
app.register_blueprint(matchScouting.bp, url_prefix = SCOUTING_PREFIX)
app.register_blueprint(pitScouting.bp, url_prefix = SCOUTING_PREFIX)



import publicity.publicityBoard as publicityBoard

app.register_blueprint(publicityBoard.bp)

manager = Manager(app)
manager.add_command('ci', CICommand(settings))

if __name__ == "__main__":
    manager.run()
