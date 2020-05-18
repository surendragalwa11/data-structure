# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/
# https://leetcode.com/problems/palindrome-partitioning/
import sys

def isPalindrome(text):
    strLen = len(text)
    mid = strLen//2
    for i in range(mid+1):
        if text[i] != text[strLen-i-1]:
            return False
    return True


def palindromePartitions(text):
    n = len(text)

    # cut array
    C = [[ 0 for i in range(n)] for i in range(n)]
    # partition array
    P = [[ False for i in range(n)] for i in range(n)]

    for i in range(n):
        C[i][i] = 0
        P[i][i] = True

    j = k = l = 0

    # l is substring length
    for l in range(2, n+1):
        # iterate over possible substrings
        for i in range(n-l+1):
            # j is ending index
            j = i + l -1

            # paritition logic
            if l == 2:
                P[i][j] = (text[i] == text[j])
            else:
                P[i][j] = ((text[i] == text[j]) and P[i+1][j-1])

            # cut logic
            if P[i][j]:
                C[i][j] = 0
            else:
                C[i][j] = sys.maxsize
                for k in range(i, j):
                    C[i][j] = min(C[i][j], C[i][k] + C[k+1][j] + 1)

    return C[0][n-1]

if __name__ == '__main__':
    text = input('Enter a string: ')
    # text = 'ababbbabbababa'
    cuts = palindromePartitions(text)
    print('/n min possible cuts:', cuts)
    # out = isPalindrome('abcefgfecba')
    # print(out)