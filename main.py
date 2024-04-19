from tokenizing import tokenize

def main():
    srcCode = "5 + 5 * 10 - 5" # one issue to fix is that tokenize does not work when there are not spaces, ex it will not work for 5*5*5
    final_list = tokenize(srcCode)
    for item in final_list:
        print(item)
    total = parserEX(final_list)
    print("the answer is: ", total)

class TreeNode:
    def __init__(self,srcToken):
        self.value = srcToken[0]
        self.token = srcToken[1]
        self.left = None
        self.right = None

def parserEX(srcList):
    if len(srcList) > 2:
        i = 0
        while i < len(srcList):
            if srcList[i][0] == '*' or srcList[i][0] == '/':
                leftTree = srcList[i-1][0] # Gets the value before the operator
                rightTree = srcList[i+1][0] # Gets the value after the operator
                if srcList[i][0] == '*':
                    result = str(int(leftTree) * int(rightTree)) # multiplys the two values 
                elif srcList[i][0] == '/':
                    result = str(int(int(rightTree) / int(leftTree))) # divides the two values
                srcList[i] = [result, 'NUMB'] 
                del srcList[i+1]
                del srcList[i-1]
                return parserEX(srcList)
            i += 1
        i = 0
        while i < len(srcList): 
            if srcList[i][0] == '+' or srcList[i][0] == '-': # checks to see if either an addition or subtraction operator was reached
                leftTree = srcList[i-1][0] # Gets the value before the operator
                rightTree = srcList[i+1][0] # Gets the value after the operator
                if srcList[i][0] == '+': # checks for an addition operator
                    result = str(int(leftTree) + int(rightTree)) # adds the two values
                elif srcList[i][0] == '-': # checks for a subtraction operator
                    result = str(int(leftTree) - int(rightTree)) # subtracts the two values
                srcList[i] = [result, 'NUMB'] # sets operator index equal to new computed value
                del srcList[i+1] # deletes index after operator from the list
                del srcList[i-1] # deletes index from before operator from the list
                return parserEX(srcList) # returns the modified list, performs recursion
            i += 1
    else:
        return srcList[0][0]
        




main()

