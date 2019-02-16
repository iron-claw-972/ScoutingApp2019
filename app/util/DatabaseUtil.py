from .DataScraper import datascraper
import mysql.connector


class DatabaseUtil:
    variableStorage = {}
    teamData = {"972": {}}
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="8characters",
        auth_plugin="mysql_native_password",
        database="app_test"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM team_info")
    print([e for e in mycursor.fetchall()])
    mydb.commit()
    # mydb.close()

    @staticmethod
    def storeVariable(name, value):
        DatabaseUtil.variableStorage[name] = value

    @staticmethod
    def addTeam(dictOfValues):
        keys = [e for e in dictOfValues]
        print('''INSERT INTO team_info('''+','.join([e for e in keys])+''')
                         VALUES('''+','.join(["'"+dictOfValues[key]+"'" for key in keys])+''')
                         ''')
        DatabaseUtil.mycursor.execute('''INSERT INTO team_info('''+','.join([e for e in keys])+''')
                         VALUES('''+','.join(["'"+dictOfValues[key]+"'" for key in keys])+''')
                         ''')

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
DatabaseUtil.addTeam(
    {"Name": "Iron Claw Robotics", "TeamNumber": "973"})
