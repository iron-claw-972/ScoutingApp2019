from flask import Flask, request, Blueprint, render_template

bp = Blueprint('liveStream', __name__)


@bp.route('/liveStream', methods=['GET'])
def handle():
    return 'data'
