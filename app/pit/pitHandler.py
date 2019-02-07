from flask import Flask, request, Blueprint, render_template, current_app
from .batteryTracker import batteryTracker

bp = Blueprint('pit', __name__)


@bp.route('/home', methods=['GET', 'POST'])
def home():
    battery1, battery2, battery3 = batteryTracker(
        current_app._get_current_object().database, request)

    return render_template('pit.html', one=battery1, two=battery2, three=battery3)
