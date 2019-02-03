from flask import Flask, request, Blueprint

bp = Blueprint('pitScouting', __name__)

@bp.route('/pitScouting', methods=['GET', 'POST'])
def handle():
    if request.method == "GET":
        return '<html><body><form action="/scouting/pit" method="POST"><input type="text" name="fname"><input type="submit" value="Submit"></form></body></html>'
    if request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        print(data)
    return data
