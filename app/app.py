import publicity.publicityBoard as publicityBoard
import scouting.scoutingHandler as scoutingHandler
import index.indexHandler as index
import pit.pitHandler as pitHandler
import util.DatabaseUtil as database
import util.DataScraper as scraper

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder="static", static_url_path="")
app.secret_key = 'no lookey lookey at me nicey long key so you are no gooooooooooood dont be him'
app.debug = True

PIT_PREFIX = '/pit'
SCOUTING_PREFIX = '/scouting'

UPLOAD_FOLDER = './static/images/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
app.allowed_file = allowed_file

def upload_file(requestFile):
    file = requestFile
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename and app.allowed_file(file.filename):
        with open("incrementUploads.txt", "r+") as incrementFile:
            currentValue = incrementFile.read()
            print(currentValue + "ooooooooooooOoOoooooHHHHH")
            filename = currentValue + "." + file.filename.split(".")[-1]
            incrementFile.truncate(0)
            incrementFile.write(str(int(currentValue) + 1))
        file.save(app.root_path + "/" + app.config['UPLOAD_FOLDER'] + "/" + filename) 
app.upload_file = upload_file

#  config, evntually move to config
app.database = database.DatabaseUtil
app.database.storeVariable('batteryStatus', ['good', 'good', 'good'])
app.database.storeVariable('timeUntilGood', [0, 0, 0])
app.database.storeVariable('batteryChargingTime', 5)

app.register_blueprint(pitHandler.bp, url_prefix=PIT_PREFIX)
app.register_blueprint(scoutingHandler.bp, url_prefix=SCOUTING_PREFIX)
app.register_blueprint(publicityBoard.bp)
app.register_blueprint(index.bp)

if __name__ == "__main__":
    app.run()
