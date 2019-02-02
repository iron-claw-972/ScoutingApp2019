from flask import Flask
import time
app = Flask(__name__)


import __init__
import pit.liveStream
#import pit.matchData
#import pit.matchSchedule
#import publicity.publicity
import scouting.matchScouting
import scouting.pitScouting
import scouting.templatingData

app.run(port=5001)
