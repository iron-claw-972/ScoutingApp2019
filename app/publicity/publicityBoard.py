from flask import Flask, request, Blueprint
import flask

bp = Blueprint('publicity', __name__, template_folder='templates')


@bp.route('/publicityBoard', methods=['GET'])
def handle():
    return flask.render_template('publicityBoard/publicityBoard.html')


@bp.route('/publicityBoard/3d', methods=['GET'])
def handle1():
    return flask.render_template('3dModel.html')
