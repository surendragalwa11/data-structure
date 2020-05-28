# https://www.geeksforgeeks.org/ugly-numbers/
def uglyNumber(n):
    uglyNumber = [0]*n
    uglyNumber[0] = 1

    i2 = i3 = i5 = 0

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, n):
        nextUglyNumber = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        uglyNumber[i] = nextUglyNumber

        if nextUglyNumber == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = uglyNumber[i2]*2
        if nextUglyNumber == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = uglyNumber[i3]*3
        if nextUglyNumber == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = uglyNumber[i5]*5

    return uglyNumber[-1]



def main():
    print(uglyNumber(150)) 


if __name__ == '__main__':
    main()