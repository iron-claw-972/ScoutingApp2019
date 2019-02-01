from flask import Flask
app = Flask(__name__)

import app.pit.batteryTracker
import app.pit.liveStream
import app.pit.matchData
import app.pit.matchSchedule
import app.scouting.matchScouting
import app.scouting.pitScouting
import app.scouting.templatingData
import app.publicity.publicity
