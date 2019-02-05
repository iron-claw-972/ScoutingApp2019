from flask import Flask, request, Blueprint
import flask

bp = Blueprint('publicity', __name__, template_folder='templates')


@bp.route('/publicityBoard', methods=['GET'])
def handle():
    return flask.render_template('publicityBoard.html')
