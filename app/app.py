from flask import Flask
app = Flask(__name__)

import scouting.matchScouting
import scouting.pitScouting
import scouting.templatingData
import pit.batteryTracker
import pit.liveStream
import pit.matchData
import pit.matchSchedule
import publicity.publicity


app.run(port=5001)
