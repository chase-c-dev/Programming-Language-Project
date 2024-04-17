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

def parserEX(srcList):
    print(srcList)
    if len(srcList) > 2:
        leftTree = TreeNode(srcList[0])
        op = TreeNode(srcList[1])
        rightTree = parserEX(srcList[2:])
    else:
        print(srcList[0])
        return TreeNode(srcList[0])
    op.left = leftTree
    op.right = rightTree
    rootNode = op

    return rootNode

main()