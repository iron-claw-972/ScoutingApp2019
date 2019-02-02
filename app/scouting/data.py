# from app import app
from flask import Flask, request, Blueprint
# import sys
# sys.path.append("..")

bp = Blueprint('bp', __name__)

@bp.route('/test', methods=['GET'])
def test():
    return "test"