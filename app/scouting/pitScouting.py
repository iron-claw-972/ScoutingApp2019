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

        if 'robotPicUpload' in request.files:
            app.upload_file(request.files['robotPicUpload'])
                

        badata = {'hatchLevelD': '', 'hatchLevelC': '', 'comments': '', 'scoutname': '', 'cargoLevelG': '', 'robotPic64': '', 'cycleTime': '', 'hatchLevel3': '', 'hatchLevel1': '', 'hatchLevel2': '', 'climbLevel': '', 'cargoLevelC': '',
                  'driveTrain': '', 'hatchLevelG': '', 'cargoComments': '', 'cargoLevel2': '', 'teamNumber': '', 'hatchComments': '', 'buddyClimb': '', 'cargoLevel3': '', 'cargoLevel1': '', 'cargoLevelD': '', 'robotPicUpload': '', 'ProgramLang': '', 'weight': ''}
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
                          'DriveTrain': badata['driveTrain'], 'ClimbLevels': badata['climbLevel'], 'CycleTime': badata['cycleTime'], 'Weight': badata['weight'], 'ProgrammingLanguage': badata['ProgramLang'], 'Comments': badata['comments']})
        print(badata)
        return render_template('fullScreenBill.html', url=requests.get('https://yesno.wtf/api/').text.split('"')[-2])
