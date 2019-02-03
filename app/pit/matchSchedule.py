from flask import Flask, request, Blueprint, render_template

bp = Blueprint('matchSchedule', __name__)


@bp.route('/matchSchedule', methods=['GET'])
def handle():
    return 'data'
