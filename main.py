from tokenizing import tokenize

def main():
    srcCode = "1 + 5 + 1 + 5 + 7"
    final_list = tokenize(srcCode)
    # for item in final_list:
    #     print(item)

    print(parserEX(final_list))

class TreeNode:
    def __init__(self,srcToken):
        self.value = srcToken[0]
        self.token = srcToken[1]
        self.left = None
        self.right = None

def parserEX(srcList):
    #print(srcList)
    if len(srcList) > 2:
        i = 0
        while i < len(srcList):
            if srcList[i][0] == '*':
                leftTree = TreeNode(srcList[i-1]) # Gets the value before the operator
                rightTree = TreeNode(srcList[i+1]) # Gets the value after the operator
                result = str(int(leftTree.value) * int(rightTree.value)) # multiplys the two values 
                srcList[i-1][0] = result # puts the resulting value back into the main list
                srcList[i-1][1] = 'NUMB' # sets the token to a number
                parserEX(srcList[i-1:i+2]) # inputs the new list getting rid of the operation thats been done 
            i += 1
        while i < len(srcList):
            if srcList[i][0] == '/':
                leftTree = TreeNode(srcList[i-1]) # Gets the value before the operator
                rightTree = TreeNode(srcList[i+1]) # Gets the value after the operator
                result = str(int(leftTree.value) * int(rightTree.value)) # multiplys the two values 
                srcList[i-1][0] = result # puts the resulting value back into the main list
                srcList[i-1][1] = 'NUMB' # sets the token to a number
                parserEX(srcList[i-1:i+2]) # inputs the new list getting rid of the operation thats been done 
            i += 1
        while i < len(srcList):
            if srcList[i][0] == '+':
                leftTree = TreeNode(srcList[i-1]) # Gets the value before the operator
                rightTree = TreeNode(srcList[i+1]) # Gets the value after the operator
                result = str(int(leftTree.value) * int(rightTree.value)) # multiplys the two values 
                srcList[i-1][0] = result # puts the resulting value back into the main list
                srcList[i-1][1] = 'NUMB' # sets the token to a number
                parserEX(srcList[i-1:i+2]) # inputs the new list getting rid of the operation thats been done 
            i += 1
        while i < len(srcList):
            if srcList[i][0] == '-':
                leftTree = TreeNode(srcList[i-1]) # Gets the value before the operator
                rightTree = TreeNode(srcList[i+1]) # Gets the value after the operator
                result = str(int(leftTree.value) * int(rightTree.value)) # multiplys the two values 
                srcList[i-1][0] = result # puts the resulting value back into the main list
                srcList[i-1][1] = 'NUMB' # sets the token to a number
                parserEX(srcList[i-1:i+2]) # inputs the new list getting rid of the operation thats been done
            i += 1 
            
            # leftTree = TreeNode(srcList[0])
            # op = TreeNode(srcList[1])
            # rightTree = parserEX(srcList[2:])

            #possibly use this
            # if srcList[i][1] in ['*', '/', '+', '-']:
            # leftTree = TreeNode(srcList[i-1]) # Gets the value before the operator
            # rightTree = TreeNode(srcList[i+1]) # Gets the value after the operator
            # if srcList[i][1] == '*':
            #     result = str(int(leftTree.value) * int(rightTree.value)) # multiplys the two values 
            # elif srcList[i][1] == '/':
            #     result = str(int(leftTree.value) / int(rightTree.value)) # divides the two values 
            # elif srcList[i][1] == '+':
            #     result = str(int(leftTree.value) + int(rightTree.value)) # adds the two values 
            # elif srcList[i][1] == '-':
            #     result = str(int(leftTree.value) - int(rightTree.value)) # subtracts the two values 
    else:
        #print(srcList[0])
        return srcList


main()

