import batteryTracker
from flask import Flask, request, Blueprint, render_template, current_app

bp = Blueprint('pit', __name__)
database = None


@bp.route('/home', methods=['GET'])
def home():
    return 'data'


@bp.route('/batteryTracker', methods=['GET', 'POST'])
def battery():
    return batteryTracker.handle(current_app._get_current_object().database, request)
