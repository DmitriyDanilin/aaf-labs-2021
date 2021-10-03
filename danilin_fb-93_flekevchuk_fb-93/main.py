from MyTokens.TokenPaterns import TokenPaterns
from Lexser import Lexer

#string = input()
a = Lexer('SELECT weight, COUNT(_id) FROM measurements WHERE height >= 170 GROUP_BY weight AA')
a.LexserAnals()

tokens  = a.getTokenArr()
for token in tokens:
    print('{type: ' + token.type + ' , text: "'+ token.text + '" , pos ' + str(token.pos) + '}')