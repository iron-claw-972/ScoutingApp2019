from .DataScraper import datascraper
import os
try:
    import mysql.connector
except:
    pass


class DatabaseUtil:
    variableStorage = {}
    teamData = {"972": {}}
    year = "2019"
    compy = "sfr"

    try:
        mydb = mysql.connector.connect(
            host="167.99.26.126",
            user="scouting",
            password=os.environ["mypass"],
            auth_plugin="mysql_native_password",
            database="app_test"
        )
        if (mydb):
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("SELECT * FROM team_info_"+year)
            # print([e for e in mycursor.fetchall()])
            mydb.commit()
        else:
            print(
                "NO SQL. you may need to obtain the password and put it into the env variable mypass")
    except Exception as e:
        print(e)
        print("NO SQL. you may need to obtain the password and put it into the env variable mypass")

    # mydb.close()

    @staticmethod
    def storeVariable(name, value):
        DatabaseUtil.variableStorage[name] = value

    @staticmethod
    def addTeam(dictOfValues):
        keys = [e for e in dictOfValues]
        DatabaseUtil.mycursor.execute('INSERT INTO team_info_'+DatabaseUtil.year+'('+','.join([e for e in keys])+''')
                         VALUES(
                             '''+','.join(["'"+dictOfValues[key]+"'" for key in keys])+''')
                         ''')
        DatabaseUtil.mydb.commit()

    @staticmethod
    def modifyTeam(teamnumber, dictOfValues):
        keys = ','.join([e+'="'+dictOfValues[e]+'"' for e in dictOfValues])
        DatabaseUtil.mycursor.execute('''UPDATE team_info_'''+DatabaseUtil.year+'''
        SET '''+keys+'''
        WHERE TeamNumber='''+teamnumber)
        DatabaseUtil.mydb.commit()

    @staticmethod
    def getTeam(teamnumber):
        DatabaseUtil.mycursor.execute(
            "SELECT * FROM team_info_"+DatabaseUtil.year)
        return [e for e in DatabaseUtil.mycursor.fetchall()]

    @staticmethod
    def matchExists(matchNumber):
        DatabaseUtil.mycursor.execute(
            'SELECT COUNT(1) FROM match_info WHERE `MatchID` = "' + matchNumber + '";')
        count = DatabaseUtil.mycursor.fetchall()[0][0]
        if(count == 0):
            return False
        elif(count == 1):
            return True
        else:
            print('Duplicate Matches!')
            quit()

    @staticmethod
    def createMatch(matchNumber):  # returns dictionary of teams
        DatabaseUtil.mycursor.execute(
            "INSERT INTO match_info (MatchID) VALUES ("+matchNumber+");")
        teamDict = datascraper.getMatchTeams(matchNumber)
        for key, value in teamDict.items():
            DatabaseUtil.mycursor.execute(
                "UPDATE match_info SET " + key + " = '" + str(value) + "' WHERE MatchID = " + matchNumber + ";")
        DatabaseUtil.mydb.commit()
        return teamDict

    @staticmethod
    def addMatchRecord(dictOfValues):
        # DatabaseUtil.mycursor.execute(
        #    'select * from team_performance where `TeamNumber`='+dictOfValues['TeamNumber'])
        keys = [e for e in dictOfValues]
        #print(["'"+dictOfValues[key]+"'" for key in keys])
        DatabaseUtil.mycursor.execute(
            'DELETE FROM team_performance_%s_%s WHERE MatchID = %s AND TeamNumber = %s' % (DatabaseUtil.year, DatabaseUtil.compy, dictOfValues['MatchID'], dictOfValues['TeamNumber']))
        DatabaseUtil.mycursor.execute('''INSERT INTO team_performance_'''+DatabaseUtil.year+'_'+DatabaseUtil.compy+'''('''+','.join([e for e in keys])+''')
                         VALUES(
                             '''+','.join(["'"+dictOfValues[key]+"'" for key in keys])+''')
                         ''')
        DatabaseUtil.mydb.commit()

    @staticmethod
    def getMatches():
        DatabaseUtil.mycursor.execute(
            "SELECT * FROM match_info")
        return DatabaseUtil.mycursor.fetchall()

    @staticmethod
    def getVariable(name):
        return DatabaseUtil.variableStorage[name]

    @staticmethod
    def writeToTeam(number, attribute, value):
        DatabaseUtil.teamData[str(number)][attribute] = value

    @staticmethod
    def getTeamData(number):
        return DatabaseUtil.teamData[str(number)]

    @staticmethod
    def addBATeamData(number):
        DatabaseUtil.teamData[number] = {}
        DatabaseUtil.teamData[number]['compResults'] = datascraper.getTeamInfo(
            number, '2018')
        DatabaseUtil.teamData[number]['teamInfo'] = datascraper.getSecretTeamInfo(
            number)


# DatabaseUtil.addBATeamData('972')
# print(DatabaseUtil.getTeamData("972"))
# print(DatabaseUtil.getMatches())
