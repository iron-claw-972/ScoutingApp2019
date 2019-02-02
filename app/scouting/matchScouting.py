# from app import app
from flask import Flask, request, Blueprint
# import sys
# sys.path.append("..")

matchScouting = Blueprint('matchScouting', __name__)

@matchScouting.route('/test2', methods=['GET'])
def handle():
    return "test2"