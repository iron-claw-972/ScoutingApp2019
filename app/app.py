from flask import Flask
import time
app = Flask(__name__)


import __init__
# import pit.liveStream
#import pit.matchData
#import pit.matchSchedule
#import publicity.publicity
# import scouting.matchScouting
# import scouting.pitScouting
# import scouting.templatingData

from scouting.data import bp

app.register_blueprint(bp)

app.run(port=5001)
