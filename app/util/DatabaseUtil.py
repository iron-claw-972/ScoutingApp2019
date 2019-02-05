
class DatabaseUtil:
    variableStorage = {}

    @staticmethod
    def storeVariable(name, value):
        DatabaseUtil.variableStorage[name] = value

    @staticmethod
    def getVariable(name):
        return DatabaseUtil.variableStorage[name]
