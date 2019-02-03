from flask import Flask, request, Blueprint

bp = Blueprint('publicityBoard', __name__)

@bp.route('/publicityBoard', methods=['GET'])
def handle():
    return 'publicityBoard'