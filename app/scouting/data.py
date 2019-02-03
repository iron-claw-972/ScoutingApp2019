from flask import Flask, request, Blueprint

bp = Blueprint('data', __name__)

@bp.route('/data', methods=['GET'])
def handle():
    return 'data'