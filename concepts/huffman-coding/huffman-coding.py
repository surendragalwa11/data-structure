class Node:
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

def huffmanTree(string):
    frequencies = {}

    # count frequency of each char
    for c in string:
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1
    
    # sort all char in descending order based on freq
    frequencies = sorted(frequencies.items(), key = lambda x: x[1], reverse = True)

    # take 2 chars with least frequencies and create a sum node as root
    nodes = frequencies
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        sumNode = Node(key1, key2)
        nodes.append((sumNode, c1+c2))

        # sort the nodes in descending order of frequencies
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    return (nodes, frequencies)

def huffmanCode(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffmanCode(l, True, binString + '0'))
    d.update(huffmanCode(r, False, binString + '1'))
    return d
    
def printHuffmanCode(frequencies, hCode):
    print(' Char | Huffman code ')
    print('--------------------')
    for (char, freq) in frequencies:
        print(' %-4r |%12s' % (char, hCode[char]))

if __name__ == '__main__':
    string = 'BCAADDDCCACACAC'
    (huffmanT, frequencies) = huffmanTree(string)
    # pass root node
    hCode = huffmanCode(huffmanT[0][0])
    # print
    printHuffmanCode(frequencies, hCode)


