from flask import Flask, request, Blueprint, render_template

bp = Blueprint('matchData', __name__)


@bp.route('/matchData', methods=['GET'])
def handle():
    return 'data'
