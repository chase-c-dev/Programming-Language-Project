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