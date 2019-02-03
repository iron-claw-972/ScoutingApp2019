from flask import Flask, request, Blueprint

bp = Blueprint('matchScouting', __name__)

@bp.route('/matchScouting', methods=['GET'])
def handle():
    return 'matchScouting'