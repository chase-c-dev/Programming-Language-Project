from tokenizing import tokenize

def main():
    srcCode = "1 + 16 / 4"
    final_list = tokenize(srcCode)
    # for item in final_list:
    #     print(item)

    total = parserEX(final_list)
    print(total)

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
                leftTree = srcList[i-1] # Gets the value before the operator
                rightTree = srcList[i+1] # Gets the value after the operator
                result = str(int(leftTree[0][0]) * int(rightTree[0][0])) # multiplys the two values 
                srcList[i] = [[result, 'NUMB']] 
                del srcList[i+1]
                del srcList[i-1]
                return parserEX(srcList)
            i += 1
        i = 0
        while i < len(srcList):
            if srcList[i][0] == '/':
                leftTree = srcList[i-1] # Gets the value before the operator
                rightTree = srcList[i+1] # Gets the value after the operator
                result = str(int(int(rightTree[0][0]) / int(leftTree[0][0]))) # divides the two values, it int casts meaning that you will not see decimals
                srcList[i] = [[result, 'NUMB']] 
                del srcList[i+1]
                del srcList[i-1]
                return parserEX(srcList)
            i += 1
        i = 0
        while i < len(srcList): 
            if srcList[i][0] == '+':
                leftTree = srcList[i-1] # Gets the value before the operator
                rightTree = srcList[i+1] # Gets the value after the operator
                print (srcList)
                result = str(int(leftTree[0][0]) + int(rightTree[0][0])) # adds the two values
                srcList[i] = [[result, 'NUMB']] 
                del srcList[i+1]
                del srcList[i-1]
                return parserEX(srcList)
            i += 1
        i = 0
        while i < len(srcList):
            if srcList[i][0] == '-':
                leftTree = srcList[i-1] # Gets the value before the operator
                rightTree = srcList[i+1] # Gets the value after the operator
                result = str(int(leftTree[0][0]) - int(rightTree[0][0])) # subtracts the two values
                srcList[i] = [[result, 'NUMB']] 
                del srcList[i+1]
                del srcList[i-1]
                return parserEX(srcList) 
            i += 1
    else:
        return srcList[0][0]

main()

