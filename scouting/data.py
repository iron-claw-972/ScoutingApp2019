from flask import Flask, request, Blueprint, render_template, current_app

bp = Blueprint('data', __name__)


def pitData():

    database = current_app._get_current_object().database

    database.mycursor.execute('describe team_info_2019')
    allcolumns=[item[0] for item in database.mycursor.fetchall()]
    allcolumns.pop(0)

    if(request.method == "GET"):
        displayed = 'none'
        return render_template('pitData.html', allcolumns=allcolumns, displayed=displayed)
    elif(request.method == "POST"):
        displayed = 'initial'

        selected = request.form.getlist("columnsSelected")
        sortBy = request.form.get("sortBy")
        sortOrder = request.form.get("sortOrder")

        database.mycursor.execute('select ' + ",".join(selected) + ' from team_info_2019 order by ' + sortBy + ' ' + sortOrder)
        data=database.mycursor.fetchall()

        return render_template('pitData.html', data=data, allcolumns=allcolumns, columns=selected, sortBy=sortBy, displayed=displayed)


def matchData():
    database = current_app._get_current_object().database
    database.mycursor.execute('select * from team_performance_2019_svr')
    return render_template('matchData.html', data=database.mycursor.fetchall())
