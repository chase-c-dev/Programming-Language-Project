# MY OTHER WAY OF DOING THE PARSER
# THIS WAY DOES NOT WORK FOR NESTED PARENTHESIS BUT EVERYTHING ELSE WORKS

# def parserEX(srcList):
#     if len(srcList) > 2:
#         i = 0
#         while i < len(srcList):
#             if srcList[i][0] == '(':
#                 j = i + 1 # starts at index after open parenthesis
#                 parenlist = []
#                 while j < len(srcList) and srcList[j][0] != ')': # start list at open parenthesis and search for another open or a close
#                     parenlist.append(srcList[j])
#                     j += 1
#                 result = parserEX(parenlist)
#                 srcList = srcList[:i] + [result] + srcList[j+1:] #[result]
#                 i = 0
#             else:
#                 i += 1
#         i = 0
#         while i < len(srcList):
#             if srcList[i][0] == '*' or srcList[i][0] == '/':
#                 leftTree = srcList[i-1][0] # Gets the value before the op
#                 rightTreeTree = srcList[i+1][0] # Gets the value after the op
#                 if srcList[i][0] == '*':
#                     result = str(int(leftTree) * int(rightTreeTree)) # multiplys the two values 
#                 elif srcList[i][0] == '/':
#                     result = str(int(int(rightTreeTree) / int(leftTree))) # divides the two values
#                 srcList[i] = [result, 'NUMB'] 
#                 del srcList[i+1]
#                 del srcList[i-1]
#                 return parserEX(srcList)
#             i += 1
#         i = 0
#         while i < len(srcList): 
#             if srcList[i][0] == '+' or srcList[i][0] == '-': # valuelookups to see if either an addition or subtraction op was reached
#                 leftTree = srcList[i-1][0] # Gets the value before the op
#                 rightTreeTree = srcList[i+1][0] # Gets the value after the op
#                 if srcList[i][0] == '+': # valuelookups for an addition op
#                     result = str(int(leftTree) + int(rightTreeTree)) # adds the two values
#                 elif srcList[i][0] == '-': # valuelookups for a subtraction op
#                     result = str(int(leftTree) - int(rightTreeTree)) # subtracts the two values
#                 srcList[i] = [result, 'NUMB'] # sets op index equal to new computed value
#                 del srcList[i+1] # deletes index after op from the list
#                 del srcList[i-1] # deletes index from before op from the list
#                 return parserEX(srcList) # returns the modified list, performs recursion
#             i += 1
#     else:
#         return srcList[0]
#     #return srcList[0]


# MY NEW WAY OF DOING THE PARSER



# This parser handles addition, multiplication, and subtract minus operations. It also handles get_evaluated_answers in parentheses. 
# The parserEX function takes a list of tokens and returns the result of the get_evaluated_answer.  
# The TreeNode class is used to build an abstract syntax tree during parsing. 
# Each TreeNode represents an operation or a number in the get_evaluated_answer. 
# The value attribute of the TreeNode is used to store the result of the operation or the number itself. 
# The token attribute is used to store the type of the token. The left and rightTree attributes are used to store the operands of the operation. 
# If the TreeNode represents a number, left and rightTree are None. 
# The parse method of the Parser class is the entry point for the parser. 
# It calls the get_evaluated_answer method to start parsing the tokens. The get_evaluated_answer method calls the addition method, which handles addition operations. 
# The addition method calls the multiplication method, which handles multiplication operations. 
# The multiplication method calls the subtract method, which handles subtract minus operations. 
# The subtract method calls the paren method, which handles numbers and get_evaluated_answers in parentheses. 
# The equals, valuelookup, move, endoflist, get_value, and get_prior methods are helper methods used to manipulate the tokens during parsing. 
# The equals method valuelookups if the tracker token has the given type and moves to the next token if it does. The valuelookup method valuelookups if the tracker token has the given type. 
# The move method moves to the next token and returns the get_prior token. The endoflist method valuelookups if all tokens have been consumed. 
# The get_value method returns the tracker token without consuming it. The get_prior method returns the get_prior token. 
# The parserEX function creates a Parser object and calls its parse method to parse the tokens. 
# It then returns the result of the get_evaluated_answer. This parser can be used with the main function and the TreeNode class in your code. 
# You can call the parserEX function with the result of the tokenize function to parse the tokens and calculate the result of the get_evaluated_answer. 
# The print("the answer is: ", total) line in the main function will then print the result of the get_evaluated_answer. 

# class Parser:
#     def __init__(self, tokens):
#         self.tokens = tokens
#         self.tracker = 0

#     def parse(self):
#         return self.get_evaluated_answer()

#     def equals(self, type_of_token):
#         if self.valuelookup(type_of_token):
#             self.move()
#             return True
#         return False

#     def valuelookup(self, type_of_token):
#         if self.endoflist():
#             return False
#         return self.get_value()[1] == type_of_token

#     def move(self):
#         if not self.endoflist():
#             self.tracker += 1
#         return self.get_prior()

#     def endoflist(self):
#         return self.tracker >= len(self.tokens)

#     def get_value(self):
#         return self.tokens[self.tracker]

#     def get_prior(self):
#         return self.tokens[self.tracker - 1]

#     def get_evaluated_answer(self):
#         return self.addition()

#     def addition(self):
#         result = self.multiplication()

#         while self.equals('PLUS') or self.equals('SUB'):
#             op = self.get_prior()
#             rightTree = self.multiplication()
#             result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

#         return result

#     def multiplication(self):
#         result = self.division()

#         while self.equals('TIMES') or self.equals('DIV'):
#             op = self.get_prior()
#             rightTree = self.division()
#             result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

#         return result
    
#     def division(self):
#         result = self.subtract()

#         while self.equals('SLASH'):
#             op = self.get_prior()
#             rightTree = self.subtract()
#             if rightTree.value == '0':
#                 raise Exception("Error: Division by zero is not allowed.")
#             result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

#         return result
    
#     def subtract(self):
#         if self.equals('SUB'):
#             op = self.get_prior()
#             rightTree = self.subtract()
#             return TreeNode([str(eval(op[0] + rightTree.value)), 'NUMB'])

#         return self.paren()

#     def paren(self):
#         if self.equals('NUMB'):
#             return TreeNode(self.get_prior())

#         if self.equals('LPAREN'):
#             result = self.get_evaluated_answer()
#             self.equals('RPAREN')
#             return result



# def addition(self):
    #     result = self.multiplication()

    #     while self.equals('PLUS'):
    #         op = self.get_prior()
    #         rightTree = self.multiplication()
    #         result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

    #     return result

    # def multiplication(self):
    #     result = self.subtract()

    #     while self.equals('TIMES'):
    #         op = self.get_prior()
    #         rightTree = self.subtract()
    #         result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

    #     return result
    
    # def division(self):
    #     result = self.subtract()

    #     while self.equals('DIV'):
    #         op = self.get_prior()
    #         rightTree = self.subtract()
    #         if rightTree.value == '0':
    #             raise Exception("Error: Division by zero is not allowed.")
    #         result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

    #     return result

    # def subtract(self):
    #     if self.equals('SUB'):
    #         op = self.get_prior()
    #         rightTree = self.subtract()
    #         return TreeNode([str(eval(op[0] + rightTree.value)), 'NUMB'])

    #     return self.paren()
