# https://www.geeksforgeeks.org/gold-mine-problem/
def getMaxGold(gold, m, n):
    goldTable = [[0 for _ in range(m)] for _ in range(n)]

    for col in range(m-1, -1, -1):
        for row in range(n):

            # right element
            if col == m-1:
                right = 0
            else:
                right = goldTable[row][col+1]

            # right top
            if row == 0 or col == m-1:
                rightTop = 0
            else:
                rightTop = goldTable[row-1][col+1]

            # right bottom
            if row == n-1 or col == m-1:
                rightBottom = 0
            else:
                rightBottom = goldTable[row+1][col+1]

            # set the max
            goldTable[row][col] = gold[row][col] + max(right, rightTop, rightBottom)
    # get the max
    maxGold = goldTable[0][0]
    for i in range(1, n):
        maxGold = max(maxGold, goldTable[i][0])
    return maxGold



def main():
    gold = [[1, 3, 1, 5], 
    [2, 2, 4, 1], 
    [5, 0, 2, 3], 
    [0, 6, 1, 2]] 
  
    m = 4
    n = 4
  
    print(getMaxGold(gold, m, n)) 


if __name__ == '__main__':
    main()