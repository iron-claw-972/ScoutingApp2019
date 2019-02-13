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
        try:
            data = database.getTeamData(number)
        except:
            database.addBATeamData(number)
            data = database.getTeamData(number)
        try:
            name = data['teamInfo']['nickname']
            website = data['teamInfo']['website']
        except:
            return flask.render_template('404.html')
        return flask.render_template('teamPages.html', num=str(number), name=data['teamInfo']['nickname'], website=website)
    
    
