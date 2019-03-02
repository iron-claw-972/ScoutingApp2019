import flask
from flask import current_app, session


def matchScouting(request):
    database = current_app._get_current_object().database
    if request.method == "GET":
        return flask.render_template('/matchScouting/inputMatchNumber.html')
    elif request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]

        data = dict(zip(fields, values))
        print(data)
        if ('teamNumber' in fields):
            database.addMatchRecord(
                {'TeamNumber': data['teamNumber'], 'MatchID': session['matchid']})
            return flask.render_template('/matchScouting/matchScouting.html', matchNumber=request.form['matchNumber'], teamNumber=request.form['teamNumber'])

        if('matchNumber' in fields):
            if(not database.matchExists(data['matchNumber'])):
                teams = database.createMatch(data['matchNumber'])
            else:
                database.mycursor.execute(
                    "select * from team_performance where `MatchID`=" + data['matchNumber'] + "")
                datateams = [e[1] for e in database.mycursor.fetchall()]
                print(datateams)
                teamlist = ['R1', 'R2', 'R3', 'B1', 'B2', 'B3']
                teams = [e for e in database.getMatches() if e[0] ==
                         data["matchNumber"]][0][1:7]
                teams = {teamlist[c]: team if not team in datateams else '' for c, team in enumerate(
                    teams)}
            print(teams)
            session['matchid'] = data['matchNumber']
            return flask.render_template('/matchScouting/inputTeamNumber.html', matchNumber=request.form['matchNumber'],
                                         R1=teams['R1'],
                                         R2=teams['R2'],
                                         R3=teams['R3'],
                                         B1=teams['B1'],
                                         B2=teams['B2'],
                                         B3=teams['B3'],)

        # example data: {'climbTime': '10', 'cargo': '1,2,1,0,', 'matchNum': '12345', 'comments': 'Comments here', 'climbLevel': 'Level 1', 'teamNum': '12345', 'hatch': '1,1,1,2,', 'sandstorm': 'idk'}
        hatchData = [e for e in data['hatch'].split(',') if e]
        cargoData = [e for e in data['cargo'].split(',') if e]
        database.addMatchRecord({"MatchID": data['matchNum'], "TeamNumber": data['teamNum'], 'Climb': data['climbLevel'], 'ClimbTime': data['climbTime'],
                                 'TopH': hatchData[3], 'MidH': hatchData[2], 'LowH': hatchData[1], 'CarH': hatchData[0], 'CarC': cargoData[0], 'LowC': cargoData[1], 'MidC': cargoData[2], 'TopC': cargoData[3], 'Comments': data['comments'], 'Sandstorm': data['sandstorm']})
        return str(data)
