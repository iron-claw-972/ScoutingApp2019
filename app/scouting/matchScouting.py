import flask
from flask import current_app


def matchScouting(request):
    if request.method == "GET":
        return flask.render_template('/matchScouting/inputMatchNumber.html')
    elif request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]

        data = dict(zip(fields, values))
        database = current_app._get_current_object().database

        if('teamNumber' in fields):
            return flask.render_template('/matchScouting/matchScouting.html', matchNumber=request.form['matchNumber'], teamNumber=request.form['teamNumber'])
        
        if('matchNumber' in fields):
            if(not database.matchExists(data['matchNumber'])):
                teams = database.createMatch(data['matchNumber'])
            return flask.render_template('/matchScouting/inputTeamNumber.html', matchNumber=request.form['matchNumber'], 
                R1 = teams['R1'],
                R2 = teams['R2'],
                R3 = teams['R3'],
                B1 = teams['B1'],
                B2 = teams['B2'],
                B3 = teams['B3'],)

    return str(data)
