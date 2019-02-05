import publicity.publicityBoard as publicityBoard
import scouting.scoutingHandler as scoutingHandler
import pit.pitHandler as pitHandler
import util.DatabaseUtil as database
from flask import Flask
from flask_script import Manager, Server
from flask_ci import CICommand
from tests import settings

app = Flask(__name__)

app.debug = True


PIT_PREFIX = '/pit'
SCOUTING_PREFIX = '/scouting'

#  config, evntually move to config
app.database = database.DatabaseUtil
app.database.storeVariable('batteryStatus', ['good', 'good', 'good'])
app.database.storeVariable('timeUntilGood', [0, 0, 0])
app.database.storeVariable('batteryChargingTime', 5)

app.register_blueprint(pitHandler.bp, url_prefix=PIT_PREFIX)
app.register_blueprint(scoutingHandler.bp, url_prefix=SCOUTING_PREFIX)
app.register_blueprint(publicityBoard.bp)

manager = Manager(app)
manager.add_command('ci', CICommand(settings))

if __name__ == "__main__":
    manager.run()
