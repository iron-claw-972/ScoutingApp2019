from flask import Flask, request, Blueprint, render_template
import time

bp = Blueprint('batteryTracker', __name__)
bp.batteryStatus = ['good', 'good', 'good']
bp.timeUntilGood = [0, 0, 0]
bp.batteryChargingTime = 5
global batteryChargingTime, batteryStatus, timeUntilGood


@bp.route('/batteryTracker', methods=['GET', "POST"])
def handle():

    if request.method == "GET":
        bp.batteryStatus = ["good" if it <
                            time.time() else "bad" for it in bp.timeUntilGood]
        return render_template('batteryTracker.html', one=bp.batteryStatus[0], two=bp.batteryStatus[1], three=bp.batteryStatus[2])
    if request.method == "POST":
        if request.form["state"] in list('012'):
            bp.batteryStatus[int(request.form["state"])] = "bad"
            bp.timeUntilGood[int(request.form["state"])
                             ] = time.time()+bp.batteryChargingTime
        return render_template('batteryTracker.html', one=bp.batteryStatus[0], two=bp.batteryStatus[1], three=bp.batteryStatus[2])
