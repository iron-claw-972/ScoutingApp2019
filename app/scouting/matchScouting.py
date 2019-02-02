from app import app
from flask import Flask, request
import sys
sys.path.append("..")
# print(app.app)

"""
@app.route('/scouting/match', methods=['GET', 'POST'])
def matchScouting():
    if request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
    return jsonify(data)
"""


@app.route("/", methods=['GET'])
def test():
    return "it works"
