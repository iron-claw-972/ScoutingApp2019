from flask import Flask, request, Blueprint
import flask

bp = Blueprint('pitScouting', __name__, template_folder='templates')

@bp.route('/pitScouting', methods=['GET', 'POST'])
def handle():
    if request.method == "GET":
        return flask.render_template('pitScouting.html')
    if request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        print(data)
    return data
