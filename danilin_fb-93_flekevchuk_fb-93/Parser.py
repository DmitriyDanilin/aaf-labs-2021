from MyTokens.Token import Token
from MyTokens.TokenPaterns import TokenPaterns
from collections import deque

class Parser:
    __tokens = []
    __pos = 0

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
    
    def parse(self):
        tokenLen = len(self.__tokens)
        if(tokenLen == 0):
            raise Exception ('Empty token array!')
        
        if(self.__tokens[0].type != "CREATETABLE" and self.__tokens[0].type != "SELECT" and self.__tokens[0].type != "DELETE" and self.__tokens[0].type != "INSERTINTO"):
            raise Exception ('Unknown comand!')

        if(self.__tokens[0].type == "CREATETABLE"):

            if(self.__tokens[1].type != "VAR"):
                raise Exception ('Incorrect table name')
            
            if(self.__tokens[2].type != "("):
                raise Exception (' ( expected ')
            
            if(self.__tokens[3].type != "VAR"):
                raise Exception (' Incorrect field name ')
            
            if(self.__tokens[tokenLen-1].type != ")"):
                raise Exception (' ) expected ')
            
            colums = deque()
            
            indexedFields = deque()

            colums.append(self.__tokens[3].text)

            oldTokenType = "VAR"

            for i in range(4 ,tokenLen):
                newTokenType = self.__tokens[i].type
                if(newTokenType != "INDEXED" and newTokenType != "COMMA" and oldTokenType == "VAR"):
                    raise Exception ('Unexpected token on position ', i)
                if(newTokenType != "VAR" and oldTokenType == "COMMA"):
                    raise Exception ('Unexpected token on position ', i)
                if(newTokenType != "COMMA" and oldTokenType == "INDEXED"):
                    raise Exception ('Unexpected token on position ', i)
                if (newTokenType == "INDEXED"):
                    indexedFields.append(self.__tokens[i-1])
                if(newTokenType == "VAR"):
                    colums.append(self.__tokens[i])
                
                #TODO: Here will be calling method to create table

        if(self.__tokens[0].type == "DELETE"):
            if(self.__tokens[1].type != "VAR"):
                raise Exception ("Unknown table name")

            if(self.__tokens[2].type != "WHERE"):
                raise Exception ("WHERE expected")
            if(self.__tokens[3].type != "VAR"):
                raise Exception ("Unknown token on position 3")
            if(self.__tokens[4].type != "EQUAL" and 
            self.__tokens[4].type != "NOT_EQUAL" and 
            self.__tokens[4].type != "MORE_EQUAL" and 
            self.__tokens[4].type != "LESS_EQUAL" and
            self.__tokens[4].type != "LESS" and
            self.__tokens[4].type != "MORE"):
                raise Exception ("Unknown token on position 4")
            if(self.__tokens[5].type != "VAR" and self.__tokens[5].type != "NUMBER"):
                raise Exception ("Unknown token on position 5")
            #TODO: Here will be calling delete method of database

        if(self.__tokens[0] == "INSERTINTO"):
            if(self.__tokens[1].type != "VAR"):
                raise Exception ("Unknown table name")
            if(self.__tokens[2].type != "("):
                 raise Exception ("( Expected")
            if(self.__tokens[tokenLen-1].type != ")"):
                 raise Exception (") Expected")

            for i in range (3,tokenLen):
                if(i % 2 == 1):
                    if (self.__tokens[i].type != "VAR"):
                        raise Exception ("Unknown token on position ", i)
                if(i % 2 == 0):
                    if (self.__tokens[i].type != "COMMA"):
                        raise Exception ("Unknown token on position ", i)
            
            #TODO: Here will be calling of insertion methood of DB
        
        if(self.__tokens[0].type == "SELECT"):
            if (self.__tokens[1].type != "VAR" and self.__tokens[1].type != "ALL"):
                 raise Exception ("Unknown token on position 1")
            
            fromPosition = 0

            if(self.__tokens[1].type == "ALL"):
                if(self.__tokens[2].type != "FROM"):
                    raise Exception ("Unknown token on position 2")
                else:
                    fromPosition = 2

            if(self.__tokens[1].type == "VAR"): #SELECT VAR1, VAR2, ... FROM
                for i in range(2, tokenLen):
                    if(self.__tokens[i].type == "FROM"):
                        fromPosition = i
                        break
                    if(i % 2 == 1):
                        if(self.__tokens[i].type != "COMMA"):
                            raise Exception ("Unknown token on position ", i)
                    if(i % 2 == 0):
                        if(self.__tokens[i].type != "VAR"):
                            raise Exception ("Unknown token on position ", i)
            if(fromPosition == 0):
                raise Exception ("From Expected")
            if(self.__tokens[fromPosition + 1].type != "VAR"):
                raise Exception ("Expected Table Name")
            

            werePosition = fromPosition + 2

            if(self.__tokens[werePosition].type != "WHERE"):
                raise Exception ("WHERE Expected")
            if(self.__tokens[werePosition+1].type != "VAR"):
                raise Exception ("Unknown token on position ", werePosition+1)
            if(
            self.__tokens[werePosition +2].type != "EQUAL" and 
            self.__tokens[werePosition +2].type != "NOT_EQUAL" and 
            self.__tokens[werePosition +2].type != "MORE_EQUAL" and 
            self.__tokens[werePosition +2].type != "LESS_EQUAL" and
            self.__tokens[werePosition +2].type != "LESS" and
            self.__tokens[werePosition +2].type != "MORE"):
                raise Exception ("Unknown token on position ", werePosition+2)
            if( self.__tokens[werePosition +3].type != "NUMBER"):
                raise Exception ("Unknown token on position ", werePosition+3)
            
            #TODO: Here will be calling select method of DB
