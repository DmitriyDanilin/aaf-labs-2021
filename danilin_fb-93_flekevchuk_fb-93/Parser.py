from AST.UnarOperationNode import UnarOperationNode
from AST.VariableNode import VariableNode
from AST.NumberNode import NumberNode
from MyTokens.Token import Token
from AST.StatementsNode import StatementsNode
from MyTokens.TokenPaterns import TokenPaterns

class Parser:
    __tokens = []
    __pos = 0
    __scope = {}

    def __init__(self, tokens):
        self.__tokens = tokens

    def __match(self, expectedTokenTypes):
        if(self.__pos < len(self.__tokens)):
            __currentToken = self.__tokens[self.__pos]
            if(__currentToken in expectedTokenTypes):
                self.__pos += 1
                return __currentToken
        return None

    def __require(self, expectedTokenTypes):
        token = self.__match(expectedTokenTypes)
        if(token == None):
            raise Exception ('On position ', self.__pos, 'expected', expectedTokenTypes[0].type)
        return token
    
    def __ParseVariable(self):
        varOrNum = self.__match(TokenPaterns.get('VAR'))
        if (varOrNum != None):
            return VariableNode(varOrNum)
    
    def __ParseUnarOperator(self):
        types = [TokenPaterns.get('SELECT'),TokenPaterns.get('DELETE'), TokenPaterns.get('INSERT INTO'),TokenPaterns.get('WHERE'),TokenPaterns.get('FROM'),TokenPaterns.get('CREATE TABLE')]
        operator = self.__match(types)
        if (operator != None):
            var = self.__ParseVariable()
            return UnarOperationNode(operator, var)
        raise Exception ('On position ', self.__pos, 'expected Key Word')

    def __pasrseExpression(self):
        unarOperationNode = self.__ParseUnarOperator()
        return unarOperationNode


    def __parseCode(self):
        root = StatementsNode()
        while(self.__pos < len(self.__tokens)):
            сodeStringNode = self.__pasrseExpression()
            #TODO: required???
            root.__addNode(сodeStringNode)
        return root

