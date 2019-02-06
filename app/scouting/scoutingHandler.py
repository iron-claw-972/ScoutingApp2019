from flask import Flask, request, Blueprint, render_template, current_app
from .pitScouting import pitScouting

bp = Blueprint('scouting', __name__)


@bp.route('/home', methods=['GET'])
def home():
    return "go to input forms"


@bp.route('/inputPitData', methods=['GET', 'POST'])
def pit():
    return pitScouting(request)
