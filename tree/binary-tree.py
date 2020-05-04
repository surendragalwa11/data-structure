class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def binarytree(arr, root, i, n):
    if i < n:
        root = Node(arr[i])
        root.left = binarytree(arr, root.left, 2*i+1, n)
        root.right = binarytree(arr, root.right, 2*i+2, n)
    return root
    
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)
    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6] 
    root = binarytree(arr, None, 0, len(arr))
    inOrder(root)


