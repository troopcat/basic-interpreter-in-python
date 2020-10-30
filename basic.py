from sys import argv
from pprint import pprint

# Lexer return type: [{}, {}, {}]
# Tokenize.tokenize return = {"PRINT":"PIRNT","LINE":10,"COL":2}

keywords = [
    "PRINT",
    "STRING"
]

class Lexer:
    
    def lex(self, fdata):

        """Vars"""

        tok = ""
        stringState = False
        string = ""
        ignore = [" ", "\t", "\n"]
        quotes = ["\"", "\'"]
        digits = ""
        digit = False
        Tokens = [] # [{"PRINT":"PRINT"}]
        linecount = 1

        """Vars"""


        for char in list(fdata):
            tok += char
            

            if stringState:
                if not char in quotes:
                    string += char

            if char in ignore and not stringState:
                tok = ""
                if char == "\n":
                    linecount += 1
        
            elif char in quotes:
                if not stringState:
                    stringState = True
                elif stringState:
                    stringState = False
                    Tokens.append({"STRING":string,"LINE":linecount})
                    string = ""
                    tok = ""

            elif tok == "PRINT":
                Tokens.append({"PRINT":"PRINT","LINE":linecount})
                tok = ""
            
            
            
            

        return Tokens


class Executer:
    def execute(self, tokens:list):
        for k,token in enumerate(tokens):
            
            # ---------------- PRINT ----------------
            if token.get("PRINT"):
                printing = list(tokens[k + 1].get("STRING"))
                for k,v in enumerate(printing):

                    if printing[k] == "\\":
                        
                        
                        printing[k] = ""
                        if printing[k + 1] == "n":
                            printing[k + 1] = ""
                            print("\n",end="")
                        elif printing[k + 1] == "t":
                            printing[k + 1] = ""
                            print("\t",end="")
                        
                        elif printing[k + 1] == "a":
                            printing[k + 1] = ""
                            print("\a",end="")
                        
                    else:
                        print(v,end="")
            
            # ---------------- STRING ----------------
            elif token.get("STRING"):
                pass
            


            
            
            



def main():
    readf = lambda filename: open(filename,"r",encoding="utf8").read()
    data = readf(argv[1])

    tokens = Lexer().lex(fdata=data)
    #pprint(tokens)
    executer = Executer()
    executer.execute(tokens)
    
    


if __name__ == "__main__":
    main()