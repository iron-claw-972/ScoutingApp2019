import flask


def matchScouting(request):
    if request.method == "GET":
        return flask.render_template('matchScouting.html')
    if request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        print(data)
    return str(data)
