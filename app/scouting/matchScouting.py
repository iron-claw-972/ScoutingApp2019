from app import app
from flask import Flask, request
import sys
sys.path.append("..")
# print(app.app)


@app.route('/scouting/match', methods=['GET', 'POST'])
def matchScouting():
    if request.method == "GET":
        return '<html><body><form action="/scouting/match" method="POST"><input type="text" name="fname"><input type="submit" value="Submit"></form></body></html>'
    if request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        print(data)
    return str(data)
