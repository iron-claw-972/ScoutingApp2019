from flask import Flask, request, Blueprint, render_template, current_app
from .pitScouting import pitScouting
from .matchScouting import matchScouting
from .teamPages import teamPages
import random
import time
bp = Blueprint('scouting', __name__)

def changeBackground():
    ilist = ['ab.jpeg','donuts.jpeg','scoutingLogo2.png','back.png','dozer.jpg','black.jpg','fish.jpeg','checker.jpg','tiger.jpg','notdirt.jpeg',
             'uploads',
             'dirt.jpeg', 'random.jpeg', 'wood.jpg']
    with open('static/css/matchScouting.css', 'w') as file:
        file.write(render_template('matchScouting.css', image="/images/"+random.choice(ilist)))
@bp.route('/home', methods=['GET'])
def home():
    return render_template('scoutingHome.html')


@bp.route('/inputPitData', methods=['GET', 'POST'])
def pit():
    return pitScouting(request)


@bp.route('/inputMatchData', methods=['GET', 'POST'])
def match():
    return matchScouting(request)

@bp.route('/pitData', methods=['GET'])
def pitDataDisplay():
    return render_template('pitData.html')

@bp.route('/matchData', methods=['GET'])
def matchDataDisplay():
    return render_template('matchData.html')

@bp.route('/teamPages')
def teamPagesInput():
    return render_template('teamPageInput.html')


@bp.route('/teamPage/<number>')
def teamPage(number):
    return teamPages(number)
