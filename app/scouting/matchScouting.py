import flask
from flask import current_app


def matchScouting(request):
    if request.method == "GET":
        return flask.render_template('matchScouting.html')
    if request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        #database = current_app._get_current_object().database
        # database.createMatch('ID'+data['fname'])
        print(data)
    return str(data)
