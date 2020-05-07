def findBadCharacter(string):
    badCharacters = [-1] * 256
    for i in range(len(string)):
        badCharacters[ord(string[i])] = i
    return badCharacters

def findPattern(string, pattern):
    m = len(pattern)
    n = len(string)

    badCharacters = findBadCharacter(pattern)

    shift = 0
    while (shift + m <= n):
        j = m - 1
        # print('shift m n j', shift, m, n, j)
        while j >=0 and string[shift + j] == pattern[j]:
            j = j - 1

        if j < 0:
            print('pattern found at index: ', shift)
            # print('found', shift, shift+m, string[shift+m], ord(string[shift+m]), badCharacters[ord(string[shift+m])])
            shift = shift + (m-badCharacters[ord(string[shift+m])] if (shift+m < n) else 1)
        else:
            # print('not found', shift, shift+j, string[shift+j], ord(string[shift+j]), badCharacters[ord(string[shift+j])], j - badCharacters[ord(string[shift+j])])
            shift = shift + max(1, j - badCharacters[ord(string[shift+j])])

if __name__ == '__main__':
    string = 'mybadcharaterhuristicalgorithofbooerandgorithmore'
    pattern = 'gorith'
    findPattern(string, pattern)
    