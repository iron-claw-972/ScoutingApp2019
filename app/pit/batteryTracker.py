from flask import Flask, request, Blueprint, render_template

bp = Blueprint('batteryTracker', __name__)


@bp.route('/batteryTracker', methods=['GET'])
def handle():
    batteryStatus = ['good', 'bad', 'good']
    return render_template('batteryTracker.html', one=batteryStatus[0], two=batteryStatus[1], three=batteryStatus[2])
