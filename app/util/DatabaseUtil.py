from .DataScraper import datascraper
try:
    import mysql.connector
except:
    pass


class DatabaseUtil:
    variableStorage = {}
    teamData = {"972": {}}
    try:
        mydb = mysql.connector.connect(
            host="167.99.26.126",
            user="root",
            password="iDevelop4Success101!",
            auth_plugin="mysql_native_password",
            database="app_test"
        )
        if (mydb):
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("SELECT * FROM team_info")
            # print([e for e in mycursor.fetchall()])
            mydb.commit()
        else:
            print("NO SQL")
    except:
        print("NO SQL")
    # mydb.close()

    @staticmethod
    def storeVariable(name, value):
        DatabaseUtil.variableStorage[name] = value

    @staticmethod
    def addTeam(dictOfValues):
        keys = [e for e in dictOfValues]
        DatabaseUtil.mycursor.execute('''INSERT INTO team_info('''+','.join([e for e in keys])+''')
                         VALUES(
                             '''+','.join(["'"+dictOfValues[key]+"'" for key in keys])+''')
                         ''')
        DatabaseUtil.mydb.commit()

    @staticmethod
    def modifyTeam(teamnumber, dictOfValues):
        keys = ','.join([e+'="'+dictOfValues[e]+'"' for e in dictOfValues])
        DatabaseUtil.mycursor.execute('''UPDATE team_info
        SET '''+keys+'''
        WHERE TeamNumber='''+teamnumber)
        DatabaseUtil.mydb.commit()

    @staticmethod
    def getTeam(teamnumber):
        DatabaseUtil.mycursor.execute("SELECT * FROM team_info")
        return [e for e in DatabaseUtil.mycursor.fetchall()]

    @staticmethod
    def addMatch(matchNumber):
        DatabaseUtil.mycursor.execute('''INSERT INTO match_info(MatchNumber)
                         VALUES(
                             '''+matchNumber+''')
                         ''')
        DatabaseUtil.mydb.commit()

    @staticmethod
    def createMatch(matchNumber):
        DatabaseUtil.mycursor.execute(
            "SELECT * FROM match_info WHERE MatchID LIKE '%" + matchNumber + "%';")
        result = DatabaseUtil.mycursor.fetchall()
        if (not result):
            DatabaseUtil.mycursor.execute(
                "INSERT INTO match_info (MatchID) VALUES ('"+matchNumber+"');")

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
