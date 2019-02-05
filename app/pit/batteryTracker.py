from flask import render_template
import time


def batteryTracker(database, request):
    if request.method == "GET":
        database.storeVariable('batteryStatus', ["good" if it < time.time(
        ) else "bad" for it in database.getVariable('timeUntilGood')])
        return database.getVariable('batteryStatus')[0], database.getVariable('batteryStatus')[1], database.getVariable('batteryStatus')[2]
    if request.method == "POST":
        if request.form["state"] in list('012'):
            batteryStatus = database.getVariable("batteryStatus")
            batteryStatus[int(request.form["state"])] = "bad"
            database.storeVariable('batteryStatus', batteryStatus)

            timeUntilGood = database.getVariable('timeUntilGood')
            batteryChargingTime = database.getVariable("batteryChargingTime")

            timeUntilGood[int(request.form["state"])
                          ] = time.time()+batteryChargingTime
            database.storeVariable('batteryStatus', batteryStatus)
        return database.getVariable('batteryStatus')[0], database.getVariable('batteryStatus')[1], database.getVariable('batteryStatus')[2]
