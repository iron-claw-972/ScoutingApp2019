from flask import Flask, request, Blueprint, render_template, current_app
import time


def batteryTracker(database, request):
    if request.method == "GET":
        database.storeVariable('batteryStatus', ["good" if it < time.time(
        ) else "bad" for it in database.getVariable('timeUntilGood')])
        return render_template('batteryTracker.html', one=database.getVariable('batteryStatus')[0], two=database.getVariable('batteryStatus')[1], three=database.getVariable('batteryStatus')[2])
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

        return render_template('batteryTracker.html', one=database.getVariable('batteryStatus')[0], two=database.getVariable('batteryStatus')[1], three=database.getVariable('batteryStatus')[2])


current_app._get_current_object().batteryTracker = batteryTracker
