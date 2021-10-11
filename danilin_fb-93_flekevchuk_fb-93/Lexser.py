from MyTokens.TokenPaterns import TokenPaterns
from MyTokens.Token import Token
import re

class Lexer:
    __pos = 0
    __code = ''
    __TokenArr = []
    def __init__(self, code):
        self.__code = code
    def getTokenArr(self):
        return self.__TokenArr
    def LexserAnals(self):
        try:
            while self.__NextToken():
                continue
        except Exception as error:
            text, pos  = error.args
            print(text + ' ' + str(pos) + ": " + self.__code[self.__pos:self.__pos + 10])

    def __NextToken(self):
        if self.__pos == (len(self.__code) - 1):
            return False
        for TokenPatern in TokenPaterns.values():
            result = re.search('^' + TokenPatern.regexp, self.__code[self.__pos:])
            if result:
                self.__pos = self.__pos + len(result[0])
                self.__TokenArr.append(Token(TokenPatern.type, result[0], self.__pos))
                return True
