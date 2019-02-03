from flask import Flask, request, Blueprint, render_template

bp = Blueprint('batteryTracker', __name__)


@bp.route('/batteryTracker', methods=['GET'])
def handle():
    return 'data'
