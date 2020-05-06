class BinaryNode:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    
    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self._add(value, self.root)

    
    def _add(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = BinaryNode(value)
            else:
                self._add(value, node.left)
        else:
            if node.right is None:
                node.right = BinaryNode(value)
            else:
                self._add(value, node.right)

    def find(self, value):
        if self.root is None:
            return None
        else:
            return self._find(value, self.root)

    def _find(self, value, node):
        if node.value == value:
            return node
        elif node.value > value and node.left is not None:
            return self._find(value, node.left)
        elif node.value < value and node.right is not None:
            return self._find(value, node.right)
    
    def printTree(self, traversalType = 0):
        if self.root is not None:
            if traversalType == 1:
                self._preOrder(self.root)
            elif traversalType == 2:
                self._postOrder(self.root)
            else:
                self._printTree(self.root)
    
    # in order traversal
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(node.value, end = ' ')
            self._printTree(node.right)
    
    def _preOrder(self, node):
        if node is not None:
            print(node.value, end = ' ')
            self._preOrder(node.left)
            self._preOrder(node.right)
    
    def _postOrder(self, node):
        if node is not None:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node.value, end = ' ')



if __name__ == '__main__':
    tree = Tree()
    nodeValues = [1, 12, 6, 5, 9]
    for val in nodeValues:
        tree.add(val)
    # traversal type 0: InOrder, 1: preOrder, 2: PostOrder
    # in order traversal
    tree.printTree()
    print('\n')
    # pre order traversal
    tree.printTree(1)
    print('\n')
    # post order traversal
    tree.printTree(2)
    print('\n')
    # find node
    node = tree.find(6)
    print(node, node.left, node.right, node.value, end = '\n')
    node = tree.find(122)
    print(node)