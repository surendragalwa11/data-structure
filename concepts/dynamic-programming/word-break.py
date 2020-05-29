# https://www.geeksforgeeks.org/word-break-problem-dp-32/

def recursiveWordBreak(wordList, word):
    if word == '':
        return True
    else:
        return any([ (word[:i] in wordList) and recursiveWordBreak(wordList, word[i:]) for i in range(1, len(word)+1)])
    #     if word[:i] in wordList and recursiveWordBreak(wordList, word[i:]):
    #         return True
    # return False


def dpWordBreak(wordList, word):
    if word == '':
        return True
    wordBreak = [False]*(len(word))

    matchedIndex = [-1]
    for i in range(len(word)):
        matchSize = len(matchedIndex)
        matched = False

        for j in range(matchSize-1, -1, -1):
            if word[matchedIndex[j]+1:i+1] in wordList:
                matched = True
                break
        
        if matched:
            wordBreak[i] = True
            matchedIndex.append(i)
    return wordBreak[len(word)-1]


def main():
    wordList = { 'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 
        'cream', 'icecream', 'man', 'go', 'mango'}
    word = 'samlikesungsamsung'
    # isAvailable = recursiveWordBreak(wordList, word)
    isAvailable = dpWordBreak(wordList, word)
    print(isAvailable)

if __name__ == '__main__':
    main()
