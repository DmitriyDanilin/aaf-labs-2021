from Lexser import Lexer
from Parser import Parser


string = 'SELECT id, name FROM map WHERE id >= 20'

def remove(str):
    return str.replace(" ", "")

stringWithoutSpaces = remove(string)

a = Lexer(stringWithoutSpaces)
a.LexserAnals()

tokens  = a.getTokenArr()
for token in tokens:
    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')

parser = Parser(tokens)
parser.parse()
