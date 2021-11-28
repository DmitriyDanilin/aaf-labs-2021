from Lexser import Lexer
from Parser import Parser
from DataBase.index import DataBase

def remove(str):
    return str.replace(" ", "")

DB = DataBase()
lexer = Lexer()
parser = Parser(DB)

queryListing = [
    'CREATE TABLE names ( var1 INDEXED, var2, var3)',
    'INSERT INTO names (1,2,3)',
    'INSERT INTO names (5,9,12)',
    'INSERT INTO names (1,2,5)',
    'INSERT INTO names (87,2,3)',
    'INSERT INTO names (13,6,3)',
    'INSERT INTO names (2,7,3)',
    #'SELECT var1, var2,var3 FROM names WHERE var1 >= -5'
    #'DELETE FROM names WHERE var1 >= 2',
    'SELECT var1, var2,var3 FROM names WHERE var1 >= -5 GROUPBY var2, var1'
    
]

queryListingForTest = [
    'SELECT COUNT(field), AVG(id), name FROM map WHERE id > 0 GROUP BY id, name'
]

#while True:
for query in queryListing:
    #print(query)
    #string = input()
    stringWithoutSpaces = remove(query)

    lexer.setCode(stringWithoutSpaces)
    lexer.LexserAnalis()
    tokens = lexer.getTokenArr()

    parser.setTokens(tokens)
    parser.parse()
    #DB.PrintDB()



'''
for token in tokens:
    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')
string = 'SELECT id, name FROM map WHERE id >= 2'
'''