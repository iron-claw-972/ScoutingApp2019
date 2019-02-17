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
        if not DatabaseUtil.mycursor.execute("SHOW TABLES LIKE '%s'" % matchNumber):
            DatabaseUtil.mycursor.execute(
                'CREATE TABLE IF NOT EXISTS '+str(matchNumber)+' (TeamNumber VARCHAR(45))')
            DatabaseUtil.mydb.commit()
            DatabaseUtil.mycursor.execute("""ALTER TABLE `app_test`.`%s`
            ADD COLUMN `TopH` VARCHAR(45) NULL AFTER `TeamNumber`,
            ADD COLUMN `MidH` VARCHAR(45) NULL AFTER `TopH`,
            ADD COLUMN `LowH` VARCHAR(45) NULL AFTER `MidH`,
            ADD COLUMN `CarH` VARCHAR(45) NULL AFTER `LowH`,
            ADD COLUMN `TopC` VARCHAR(45) NULL AFTER `CarH`,
            ADD COLUMN `MidC` VARCHAR(45) NULL AFTER `TopC`,
            ADD COLUMN `LowC` VARCHAR(45) NULL AFTER `MidC`,
            ADD COLUMN `CarC` VARCHAR(45) NULL AFTER `LowC`,
            ADD COLUMN `Climb` VARCHAR(45) NULL AFTER `CarC`,
            ADD PRIMARY KEY (`TeamNumber`);""" % (str(matchNumber)))

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
