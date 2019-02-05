from flask import Flask, request, Blueprint, render_template, current_app


bp = Blueprint('pit', __name__)
database = None


@bp.route('/home', methods=['GET'])
def home():
    return 'data'


@bp.route('/batteryTracker', methods=['GET', 'POST'])
def batteryTracker():
    database = current_app._get_current_object().database
    database.storeVariable("charge", 1)
    return str(database.getVariable("charge"))
