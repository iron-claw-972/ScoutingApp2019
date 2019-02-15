from flask import Flask, request, Blueprint, render_template, current_app
from .pitScouting import pitScouting
from .matchScouting import matchScouting
from .teamPages import teamPages

bp = Blueprint('scouting', __name__)


@bp.route('/home', methods=['GET'])
def home():
    return render_template('scoutingHome.html')


@bp.route('/inputPitData', methods=['GET', 'POST'])
def pit():
    return pitScouting(request)


@bp.route('/inputMatchData', methods=['GET', 'POST'])
def match():
    return matchScouting(request)

@bp.route('/data', methods=['GET'])
def currentDataDisplay():
    return render_template('currentData.html')


@bp.route('/teamPages')
def teamPagesInput():
    return render_template('teamPageInput.html')


@bp.route('/teamPage/<number>')
def teamPage(number):
    return teamPages(number)
