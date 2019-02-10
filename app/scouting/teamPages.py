import flask
from flask import current_app


def teamPages(number):
    database = current_app._get_current_object().database
    try:
        data = database.getTeamData(number)
    except:
        database.addBATeamData(number)
        data = database.getTeamData(number)
    try:
        name = data['teamInfo']['nickname']
    except:
        return flask.render_template('404.html')
    return flask.render_template('teamPages.html', num=str(number), name=data['teamInfo']['nickname'])
