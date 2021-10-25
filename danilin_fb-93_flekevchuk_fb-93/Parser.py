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
    
    def Insert(self, tokenLen):
        varsToInsert = deque()
        tableName = ""

        if(self.__tokens[1].type != "VAR"):
            raise Exception ("Unknown table name")
        tableName = self.__tokens[1].text
        if(self.__tokens[2].type != "("):
            raise Exception ("( Expected")
        if(self.__tokens[tokenLen-1].type != ")"):
            raise Exception (") Expected")

        for i in range (3,tokenLen):# INSERT INTO name (var1,var2,...)
            if(self.__tokens[i].type == ")"):
                break
            if(i % 2 == 1):
                if (self.__tokens[i].type != "VAR"):
                    raise Exception ("Unknown token on position ", i)
                varsToInsert.append(self.__tokens[i].text)
            if(i % 2 == 0):
                if (self.__tokens[i].type != "COMMA"):
                    raise Exception ("Unknown token on position ", i)
            
            #TODO: Here will be calling of insertion methood of DB
        print("Insert into "+ tableName + " inserted: " )
        print(varsToInsert)
    
    def CreateTable(self, tokenLen):

            colums = deque()
            
            indexedFields = deque()

            tableName = ""

            if(self.__tokens[1].type != "VAR"):
                raise Exception ('Incorrect table name')
            tableName = self.__tokens[1].text
            if(self.__tokens[2].type != "("):
                raise Exception (' ( expected ')
            
            if(self.__tokens[3].type != "VAR"):
                raise Exception (' Incorrect field name ')
            
            if(self.__tokens[tokenLen-1].type != ")"):
                raise Exception (' ) expected ')
            
            

            colums.append(self.__tokens[3].text)

            oldTokenType = "VAR"
            if(tokenLen > 5):
                for i in range(4 ,tokenLen):
                    newTokenType = self.__tokens[i].type
                    if(newTokenType != "INDEXED" and newTokenType != "COMMA" and newTokenType != ")" and oldTokenType == "VAR"):
                        raise Exception ('Unexpected token on position ', i)
                    if(newTokenType != "VAR" and oldTokenType == "COMMA"):
                        raise Exception ('Unexpected token on position ', i)
                    if(newTokenType != "COMMA" and oldTokenType == "INDEXED"):
                        raise Exception ('Unexpected token on position ', i)
                    if(newTokenType == ")" and (oldTokenType != "VAR" and oldTokenType != "INDEXED")):
                        raise Exception ('Unexpected ) on position ', i)
                    if (newTokenType == "INDEXED"):
                        indexedFields.append(self.__tokens[i-1].text)
                        oldTokenType = "INDEXED"
                    if(newTokenType == "VAR"):
                        colums.append(self.__tokens[i].text)
                        oldTokenType = "VAR"
                    if(newTokenType == "COMMA"):
                        oldTokenType = "COMMA"
            print("Table " + tableName +" created")
            print("coloms")
            print(colums) 
            print("Indexed fields")
            print(indexedFields)  

                #TODO: Here will be calling method to create table
    def Delete(self, tokenLen):
        if(self.__tokens[1].type != "FROM"):
            raise Exception ("FROM expected")
        if(self.__tokens[2].type != "VAR"):
            raise Exception ("Unknown table name")

        if(self.__tokens[3].type != "WHERE"):
            raise Exception ("WHERE expected")
        if(self.__tokens[4].type != "VAR"):
            raise Exception ("Unknown token on position 4")
        if(self.__tokens[5].type != "EQUAL" and 
        self.__tokens[5].type != "NOT_EQUAL" and 
        self.__tokens[5].type != "MORE_EQUAL" and 
        self.__tokens[5].type != "LESS_EQUAL" and
        self.__tokens[5].type != "LESS" and
        self.__tokens[5].type != "MORE"):
            raise Exception ("Unknown token on position 5")
        if(self.__tokens[6].type != "VAR" and self.__tokens[5].type != "NUMBER"):
            raise Exception ("Unknown token on position 6")
            #TODO: Here will be calling delete method of database
        print("Deleting from " + self.__tokens[2].text)

    def Select(self, tokenLen):
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
                if(i % 2 == 0):
                    if(self.__tokens[i].type != "COMMA"):
                        raise Exception ("Unknown token on position ", i)
                if(i % 2 == 1):
                    if(self.__tokens[i].type != "VAR"):
                        raise Exception ("Unknown token on position ", i)
        if(fromPosition == 0):
            raise Exception ("From Expected")
        if(self.__tokens[fromPosition + 1].type != "VAR"):
            raise Exception ("Expected Table Name")
            

        werePosition = fromPosition + 2
        if(werePosition < tokenLen):
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
            if( self.__tokens[werePosition +3].type != "VAR"):
                raise Exception ("Unknown token on position ", werePosition+3)
        #TODO: Here will be calling select method of DB
    
            
            
    def parse(self):
        tokenLen = len(self.__tokens)
        if(tokenLen == 0):
            raise Exception ('Empty token array!')
        
        if(self.__tokens[0].type != "CREATETABLE" and self.__tokens[0].type != "SELECT" and self.__tokens[0].type != "DELETE" and self.__tokens[0].type != "INSERTINTO"):
            raise Exception ('Unknown comand!')

        if(self.__tokens[0].type == "CREATE TABLE"):
            self.CreateTable(tokenLen)

        if(self.__tokens[0].type == "DELETE"):
            self.Delete(tokenLen)

        if(self.__tokens[0].type == "INSERT INTO"):
            self.Insert(tokenLen)
        
        if(self.__tokens[0].type == "SELECT"):
            self.Select(tokenLen)
