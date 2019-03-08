import flask
from flask import current_app, session, render_template
import requests

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename


def pitScouting(request):
    app = current_app._get_current_object()

    database = current_app._get_current_object().database
    if request.method == "GET":
        return flask.render_template('pitScouting.html')
    if request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        filenumber = ""
        if 'robotPicUpload' in request.files:
            file = request.files['robotPicUpload']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename and app.allowed_file(file.filename):
                with open("scouting/incrementUploads.txt", "r+") as incrementFile:

                    currentValue = incrementFile.read()
                    print("CURRENT VALUE IS " + currentValue)
                    filename = currentValue
                    filenumber = currentValue
                    incrementFile.seek(0)
                    incrementFile.write(str(int(currentValue) + 1))
                    incrementFile.truncate(0)
                file.save(app.root_path + "/" +
                          app.config['UPLOAD_FOLDER'] + "/" + filename)

        badata = {'hatchLevelD': None, 'hatchLevelC': None, 'comments': None, 'scoutname': None, 'cargoLevelG': None, 'robotPic64': None, 'cycleTime': None, 'hatchLevel3': None, 'hatchLevel1': None, 'hatchLevel2': None, 'climbLevel': None, 'cargoLevelC': None,
                  'driveTrain': None, 'hatchLevelG': None, 'cargoComments': None, 'cargoLevel2': None, 'teamNumber': None, 'hatchComments': None, 'buddyClimb': None, 'cargoLevel3': None, 'cargoLevel1': None, 'cargoLevelD': None, 'robotPicURL': None, 'ProgramLang': None, 'weight': None, 'scoutname': None}
        badata.update(data)
        cargoIntake = ('D' if badata['cargoLevelD'] == 'on' else '') + \
            ('G' if badata['cargoLevelG'] == 'on' else '')
        hatchIntake = ('D' if badata['hatchLevelD'] == 'on' else '') + \
            ('G' if badata['hatchLevelG'] == 'on' else '')
        cargoOutake = ('C' if badata['cargoLevelC'] == 'on' else '') + ('1' if badata['cargoLevel1'] == 'on' else '') + (
            '2' if badata['cargoLevel2'] == 'on' else '') + ('3' if badata['cargoLevel3'] == 'on' else '')
        hatchOutake = ('C' if badata['hatchLevelC'] == 'on' else '') + ('1' if badata['hatchLevel1'] == 'on' else '') + (
            '2' if badata['hatchLevel2'] == 'on' else '') + ('3' if badata['hatchLevel3'] == 'on' else '')

        database.addTeam({'TeamNumber': badata['teamNumber'], 'HatchLevels': hatchOutake, 'CargoLevels': cargoOutake, 'HatchIntake': hatchIntake, 'CargoComments': badata['cargoComments'], 'CargoIntake': cargoIntake, 'HatchComments': badata['hatchComments'],
                          'DriveTrain': badata['driveTrain'], 'ClimbLevels': badata['climbLevel'], 'CycleTime': badata['cycleTime'], 'Weight': badata['weight'], 'ProgrammingLanguage': badata['ProgramLang'], 'Comments': badata['comments'], "Picture": filenumber, "ScouterName": badata['scoutname']})
        print(badata)
        return render_template('fullScreenBill.html', url=requests.get('https://yesno.wtf/api/').text.split('"')[-2])
