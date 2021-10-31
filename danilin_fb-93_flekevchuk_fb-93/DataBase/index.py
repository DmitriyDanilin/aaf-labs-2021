from DataBase.Table import Table


class DataBase:
    def __init__(self):
        self.dataBase = {}
        self.allTablesName = []
    def PrintDB(self):
        for Table in  self.allTablesName:
            Tab = self.dataBase[Table]
            print(Tab.columns)
            print(Tab.indexedColumns)
            print(Tab.table)
            for key in Tab.indexes.keys():
                print(key, end=": ")
                Tab.indexes[key].PrintTree()
                print()

    def DoseTableExist(self, name):
        if name not in self.allTablesName:
            raise Exception ('There is no table with name', name)

    def CreateTable(self, name, columns, indexes):
        if name not in self.allTablesName:
            self.allTablesName.append(name) 
            self.dataBase[name] = Table(columns, indexes)
        else :
            raise Exception ('Table with this name already exists')

    def Insert(self, name, varsToInsert):
        self.DoseTableExist(name)
        self.dataBase[name].CheckNumberOfColumns(len(varsToInsert))
        self.dataBase[name].Insert(varsToInsert)

    def Delete(self, name, param1, condition, param2):
        self.DoseTableExist(name)
        toCheck = []
        if param1.type == 'VAR':
            toCheck.append(param1)
        if param2.type == 'VAR':
            toCheck.append(param2)  
        self.dataBase[name].CheckIfInColumns(toCheck)
        self.dataBase[name].Delete(param1, condition, param2)



    





