from flask import Flask
import time
app = Flask(__name__)


# import __init__
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

app.run(port=5001)
