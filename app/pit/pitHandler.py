from flask import Flask, request, Blueprint, render_template, current_app
from .batteryTracker import batteryTracker
from .matchSchedule import matchSchedule
bp = Blueprint('pit', __name__)


@bp.route('/home', methods=['GET', 'POST'])
def home():
    scraper = current_app._get_current_object().scraper
    battery1, battery2, battery3 = batteryTracker(
        current_app._get_current_object().database, request)
    AP1, OT1, T1, AP2, OT2, T2 = matchSchedule(scraper)
    return render_template('pit.html', one=battery1, two=battery2, three=battery3, AP1=AP1, OT1=OT1, T1=T1, AP2=AP2, OT2=OT2, T2=T2)
