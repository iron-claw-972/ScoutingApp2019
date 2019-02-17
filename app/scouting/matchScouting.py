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
        #database.createMatch('ID'+data['matchNumber'])
        print(data)

        if('teamNumber' in fields):
            return flask.render_template('/matchScouting/matchScouting.html', matchNumber=request.form['matchNumber'], teamNumber=request.form['teamNumber'])
        if('matchNumber' in fields):
            return flask.render_template('/matchScouting/inputTeamNumber.html', matchNumber=request.form['matchNumber'])

    return str(data)
