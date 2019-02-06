from flask import render_template
import datetime


def matchSchedule(database, request):
    currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
