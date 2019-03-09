import flask
from flask import current_app
from random import randint


def teamPages(number):

    if(not str(number).isdigit()):
        try:
            return teamPages(str(randint(1, 3790)))
        except:
            return teamPages(str(randint(1, 3790)))

    else:
        database = current_app._get_current_object().database
        try:
            database.addBATeamData(number)
            generalData = database.getTeamData(number)
            robotData = database.getTeam(number)
            if not robotData:
                robotData = [['' for e in range(20)]]

            name = generalData['teamInfo']['nickname']
            website = generalData['teamInfo']['website']
        except:
            return flask.render_template('404.html')
        print(robotData)
        PHH = (robotData[0][3])
        PCH = (robotData[0][4])
        HIL = (robotData[0][5])
        CIL = (robotData[0][7])
        BC = ("Yes" if robotData[0][11] == 'on' else 'No')
        PL = (robotData[0][14])
        DT = (robotData[0][9])
        COM = (robotData[0][-2])
        CT = (robotData[0][12])
        W = (robotData[0][13])
        HC = (robotData[0][8])
        CC = (robotData[0][6])
        PIC = ("/images/uploads/"+str(robotData[0][-1]))
        matches = database.getTeamMatchPerformance(number)
        return flask.render_template('teamPages.html', HC=HC, CC=CC, CT=CT, W=W, PL=PL, DT=DT, COM=COM, BC=BC, PIC=PIC, HIL=HIL, PHH=PHH, PCH=PCH, CIL=CIL, num=str(number), name=name, website=website, matches=matches)
