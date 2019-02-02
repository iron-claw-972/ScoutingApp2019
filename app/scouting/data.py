# from app import app
from flask import Flask, request, Blueprint
# import sys
# sys.path.append("..")

bp = Blueprint('data', __name__)

@bp.route('/test', methods=['GET'])
def handle():
    return "test"