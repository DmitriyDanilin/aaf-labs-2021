from DataBase.Tree import Node
from DataBase.BinaryOperators import allBinares

class Table:
    def __init__(self, columns, indexesColumn):
        self.table = list()
        self.indexedColumns = list()
        self.indexes = dict()
        self.columns = list(columns)
        for index in indexesColumn:
            i = 0
            for column in columns:
                if column == index:
                    self.indexedColumns.append([column,i])
                    break
                i+=1
            self.indexes[index] = Node(None, None)

    def Insert(self, varsToInsert):
        id = len(self.table)
        self.table.append(varsToInsert)
        for idColumns in self.indexedColumns:
            self.indexes[idColumns[0]].insert(varsToInsert[idColumns[1]], id)

    def CheckNumberOfColumns(self, length):
        if length != len(self.columns):
            raise Exception ('Table has this number of columns ', len(self.columns))

    def CheckIfInColumns(self,columns):
        allCorrectColumns = len([column for column in columns if column.text in self.columns])
        if len(columns) != allCorrectColumns:
            raise Exception ('There is no such columns as',
            [column for column in columns if column not in self.columns] )

    def Delete(self, param1, condition, param2):
        allIDs = self.select(param1, condition, param2)
        for id in allIDs:
            for index in self.indexedColumns:
                print(index[0])
                self.indexes[index[0]].DeleteWithID(self.table[id][index[1]], id)
            self.table[id] = None

    def select(self, param1, condition, param2):
        if param1.type == param2.type:
            #return self.ParsIndexCondition(param1.text, condition, param2.text)
            pass
        elif param1.type == 'VAR':
            if  param1.text in self.indexes.keys():
                return self.ParsIndexCondition(param1.text, condition, int(param2.text))
            return self.ParsCondition(param1.text, condition, int(param2.text))
        elif param2.type == 'VAR':
            if param2.text in self.indexes.keys():
                return self.ParsIndexCondition(param2.text, condition, int(param1.text))
            return self.ParsCondition(param2.text, condition, int(param1.text))

    def ParsIndexCondition(self, index, condition, number):
        if condition.type == 'EQUAL':
            return self.indexes[index].find(number)
        if condition.type == 'NOT_EQUAL':
            return self.indexes[index].find(number)
        if condition.type == 'MORE_EQUAL':
            return self.indexes[index].getAllIDsMore(number, True)
        if condition.type == 'MORE':
            return self.indexes[index].getAllIDsMore(number, False)
        if condition.type == 'MORE_LESS':
            return self.indexes[index].getAllIDsLess(number, True)
        if condition.type == 'LESS':
            return self.indexes[index].getAllIDsLess(number, False)

    def ParsCondition(self, column, condition, number):
        columnID = self.columns.index(column)
        i = 0
        allIDs = []
        binaryCondition = allBinares[condition.type](number, columnID)
        for row in self.table:
            if binaryCondition(row):
                allIDs.append(i)
            i+=1
        return allIDs
        
        
            

        




'''
'EQUAL': lambda a, b: a==b,
    'NOT_EQUAL': lambda a, b: a!=b,
    'MORE_EQUAL': lambda a, b: a>=b,
    'LESS_EQUAL': lambda a, b: a<=b,
    'LESS': lambda a, b: a<b,
    'MORE': lambda a, b: a>b
'''
        