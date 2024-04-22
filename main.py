from tokenizing import tokenize

def main():
    srcCode = "( 5 * ( 5 + 5 ) / 2 ) - 2" # one issue to fix is that tokenize does not work when there are not spaces, ex it will not work for 5*5*5 even (5*5*5) will not work
    final_list = tokenize(srcCode)
    for item in final_list:
        print(item)
        parser = ParserEX(final_list)
    total = parser.addition().value
    print("the answer is: ", total)

class TreeNode:
    def __init__(self,srcToken):
        self.value = srcToken[0]
        self.token = srcToken[1]
        self.left = None
        self.rightTree = None

class ParserEX:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.tracker = 0

    def equals(self, type_of_token):
        total = 0
        if self.tracker < len(self.tokens):
            total = self.tokens[self.tracker][1] == type_of_token
        if self.tracker >= len(self.tokens):
            total = False
        if total:
            if not self.tracker >= len(self.tokens):
                self.tracker += 1
            self.tokens[self.tracker - 1]
            return True
        return False

    def addition(self):
        result = self.multiplication()

        while self.equals('PLUS') or self.equals('SUB'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.multiplication()
            result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

        return result

    def multiplication(self):
        result = self.division()

        while self.equals('TIMES') or self.equals('DIV'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.division()
            result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

        return result
    
    def division(self):
        result = self.subtract()

        while self.equals('SLASH'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.subtract()
            result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

        return result
    
    def subtract(self):
        if self.equals('SUB'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.subtract()
            return TreeNode([str(eval(op[0] + rightTree.value)), 'NUMB'])

        return self.paren()

    def paren(self):
        if self.equals('NUMB'):
            return TreeNode(self.tokens[self.tracker - 1])
        if self.equals('LPAREN'):
            result = self.addition()
            self.equals('RPAREN')
            return result

main()

