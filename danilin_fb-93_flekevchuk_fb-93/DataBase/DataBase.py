class Table:

    table = {}
    columns = []

    def __init__(self,columns):
        for column in columns:
            self.table[column]=[]
            self.columns.append(column)

    def Insert(self, varsToInsert):
        i = 0
        for column in self.columns:
            self.table[column].append(varsToInsert[i])
            i+=1

    def CheckNumberOfColumns(self, length):
        if length != len(self.columns):
            raise Exception ('Table has this number of columns ', len(self.columns))
            
    def CheckIfInColumns(self,columns):
        allCorrectColumns = len([column for column in columns if column in self.columns])
        if len(columns) != len(allCorrectColumns):
            raise Exception ('There is no such columns as',
            [column for column in columns if column not in self.columns] )
        

class DataBase:
    dataBase = {}
    allTablesName = []
    def __init__(self):
        pass

    def IsTableExist(self, name):
        if name not in self.allTablesName:
            raise Exception ('There is no table with name', name)

    def CreateTable(self, name, columns):
        if name not in self.allTablesName:
            self.allTablesName.append(name) 
            self.dataBase[name] = Table(columns)
        else :
             raise Exception ('Table with this name already exists')

    def Insert(self, name, varsToInsert):
        self.IsTableExist(name)
        self.dataBase[name].CheckNumberOfColumns(len(varsToInsert))
        self.dataBase[name].Insert(varsToInsert)