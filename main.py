from tokenizing import tokenize

def main():
    srcCode = "1 + 5 + 1 + 5 + 7"
    final_list = tokenize(srcCode)
    for item in final_list:
        print(item)

    parserEX(final_list)

class TreeNode:
    def __init__(self,srcToken):
        self.value = srcToken[0]
        self.token = srcToken[1]
        self.left = None
        self.right = None

    def evaluate(self):
        if self.token == "NUMBER":
            return int(self.value)
        elif self.token == "PLUS":
            return self.left.evaluate() + self.right.evaluate()
        elif self.token == "MINUS":
            return self.left.evaluate() - self.right.evaluate()
        elif self.token == "MULTIPLY":
            return self.left.evaluate() * self.right.evaluate()
        elif self.token == "DIVIDE":
            return self.left.evaluate() / self.right.evaluate()

def parserEX(srcList):
    #print(srcList)
    if len(srcList) > 2:
        leftTree = TreeNode(srcList[0])
        op = TreeNode(srcList[1])
        rightTree = parserEX(srcList[2:])
        op.left = leftTree
        op.right = rightTree
        rootNode = op
    elif len(srcList) == 2:
        leftTree = TreeNode(srcList[0])
        op = TreeNode(srcList[1])
        rootNode = op
    else:
        return TreeNode(srcList[0])

    return rootNode

    # print(srcList)
    # if len(srcList) > 2:
    #     leftTree = TreeNode(srcList[0])
    #     op = TreeNode(srcList[1])
    #     rightTree = parserEX(srcList[2:])
    # else:
    #     print(srcList[0])
    #     return TreeNode(srcList[0])
    # op.left = leftTree
    # op.right = rightTree
    # rootNode = op

    # return rootNode

main()

