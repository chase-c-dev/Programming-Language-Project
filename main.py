from tokenizing import tokenize

def main():
    srcCode = "( 5 * ( 5 + 5 ) / 2 ) - 2" # one issue to fix is that tokenize does not work when there are not spaces, ex it will not work for 5*5*5 even (5*5*5) will not work
    #srcCode = "5 / 5 * 2"
    #srcCode = "5 - 20 + 5 + 5"
    final_list = tokenize(srcCode)
    for item in final_list:
        print(item)
        parser = ParserEX(final_list)
    total = parser.addition().value
    print("the answer is: ", total)

class TreeNode: # used to build tree during parsing
    def __init__(self,srcToken):
        self.value = srcToken[0] # stores result of a operation or a number
        self.token = srcToken[1] # stores the token relating to the type of the node
        self.left = None
        self.rightTree = None

# Parses through the input tokenized list and evaluates it, starts out in the addition function which loops through all the functions checking each operation
# The equals function is what increments through the tokens as well as performs token checks to determine what order to perform the operations
class ParserEX:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.tracker = 0

    def addition(self): # addition is called first
        result = self.multiplication() # calls multiplication which handles the multiplication operations
        while self.equals('PLUS') or self.equals('SUB'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.multiplication()
            result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

        return result

    def multiplication(self): # checks multiplication and division
        result = self.division() # calls division which handles division operations
        while self.equals('TIMES') or self.equals('DIV'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.division()
            result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

        return result
    
    def division(self): # checks division 
        result = self.subtract() # calls subtraction which handles subtraction operations
        while self.equals('DIV'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.subtract()
            result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

        return result
    
    def subtract(self): # checks subtraction
        if self.equals('SUB'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.subtract()
            return TreeNode([str(eval(op[0] + rightTree.value)), 'NUMB'])

        return self.paren()

    def paren(self):
        if self.equals('NUMB'): # if tree node is a NUMB then both trees are None and you return the current NUMB node
            return TreeNode(self.tokens[self.tracker - 1])
        if self.equals('LPAREN'):
            result = self.addition() # goes back up to addition
            self.equals('RPAREN')
            return result
    
    def equals(self, type_of_token): # used to check tokens for operators and alter the tokens throughout the parse
        total = 0
        if self.tracker < len(self.tokens) and self.tokens[self.tracker][1] == type_of_token: # makes sure to only set total to a token if the list index is within bounds and the tokens match up
            self.tokens[self.tracker][1] == type_of_token
            total = self.tokens[self.tracker][1] # sets total equal to current token
        if self.tracker >= len(self.tokens): # returns False if the list index kept by tracker is out of bounds
            total = False
        if total: 
            if self.tracker < len(self.tokens): # checks once again to make sure tracker is not out of bounds 
                self.tracker += 1 # increments tracker (moves to next token)
            return True 
        return False

main()

