from collections import defaultdict

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root
        self.tree = defaultdict()
        self.tree[root.val] = -1

    def getTreeRoot(self):
        return self.root
    
    def addNode(self, parentVal, isLeftChild, nodeVal):
        if self.root is None:
            return
        else:
            self._addNode(self.root, parentVal, isLeftChild, nodeVal)

    def _addNode(self, root, parentVal, isLeftChild, nodeVal):
        if root is None:
            return
        if root.val == parentVal:
            if isLeftChild:
                root.left = Node(nodeVal)
                self.tree[nodeVal] = root.val
            else:
                root.right = Node(nodeVal)
                self.tree[nodeVal] = root.val
        else:
            if root.left:
                self._addNode(root.left, parentVal, isLeftChild, nodeVal)
            if root.right:
                self._addNode(root.right, parentVal, isLeftChild, nodeVal)

def isCousions(node, parentDict, heightDict, height):
    if not node:
            return
    if node.left:
        heightDict[node.left.val] = height+1
        parentDict[node.left.val] = node.val
        isCousions(node.left, parentDict, heightDict, height+1)
    if node.right:
        heightDict[node.right.val] = height+1
        parentDict[node.right.val] = node.val
        isCousions(node.right, parentDict, heightDict, height+1)
    
    return parentDict, heightDict

if __name__ == '__main__':
    rootNode = Node(1)
    t = Tree(rootNode)

    t.addNode(1, True, 2)
    t.addNode(1, False, 3)

    t.addNode(2, False, 4)
    t.addNode(3, False, 5)

    x = 5
    y = 4

    # print(t.getTreeRoot())
    # print(t.tree)
    heightDict = {}
    parentDict = {}

    # initialise for root
    heightDict[rootNode.val] = 0
    parentDict[rootNode.val] = 0

    
    parentDict, heightDict = isCousions(t.getTreeRoot(), parentDict, heightDict, 0)
    # print(heightDict, parentDict)

    # is cousions
    if parentDict[x] != parentDict[y] and heightDict[x] == heightDict[y]:
        print('Yes! They are cousions.')
    else:
        print('No! They lied you! They are not cousions.')

# Problem Statement: Two nodes of a binary tree are cousins if they have the same depth, but have different parents.