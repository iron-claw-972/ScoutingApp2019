from flask import Flask, request, Blueprint, render_template

bp = Blueprint('pit', __name__)


@bp.route('/home', methods=['GET'])
def handle():
    return 'data'
