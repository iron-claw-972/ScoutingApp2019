import flask
from flask import current_app
from random import randint


def teamPages(number):
    if(str(number) == "random"):
        try:
            return teamPages(str(randint(1, 3790)))
        except:
            return teamPages(str(randint(1, 3790)))
    else:
        database = current_app._get_current_object().database
        database.addBATeamData(number)
        generalData = database.getTeamData(number)
        robotData = database.getTeam(number)
        try:
            name = generalData['teamInfo']['nickname']
            website = generalData['teamInfo']['website']
        except:
            return flask.render_template('404.html')

        PHH = (robotData[0][3])
        PCH = (robotData[0][4])
        HIL = (robotData[0][5])
        CIL = (robotData[0][7])
        matches = database.getTeamMatchPerformance(number)    
        return flask.render_template('teamPages.html', HIL=HIL, PHH=PHH, PCH=PCH, CIL=CIL, num=str(number), name=name, website=website, matches=matches)
