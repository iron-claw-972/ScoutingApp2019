from flask import Flask, request, Blueprint, render_template, current_app

bp = Blueprint('data', __name__)


def pitData():
    database = current_app._get_current_object().database
    database.mycursor.execute('select * from team_info_2019')
    return render_template('pitData.html', data=database.mycursor.fetchall())


def matchData():
    database = current_app._get_current_object().database
    database.mycursor.execute('select * from team_performance_2019_sfr')
    return render_template('matchData.html', data=database.mycursor.fetchall())
