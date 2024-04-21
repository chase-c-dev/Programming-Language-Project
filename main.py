from tokenizing import tokenize

def main():
    srcCode = "( 2 * ( 5 + 5 + 5 ) + 5 )" # one issue to fix is that tokenize does not work when there are not spaces, ex it will not work for 5*5*5 even (5*5*5) will not work
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
            if srcList[i][0] == '(':
                j = i + 1 # starts at index after open parenthesis
                parenlist = []
                while j < len(srcList) and srcList[j][0] != ')': # start list at open parenthesis and search for another open or a close
                    parenlist.append(srcList[j])
                    j += 1
                result = parserEX(parenlist)
                srcList = srcList[:i] + [result] + srcList[j+1:] #[result]
                i = 0
            else:
                i += 1
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
        return srcList[0]
    #return srcList[0]




main()

