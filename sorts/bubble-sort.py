# Normal Solution
# def bubbleSort(fullList):
#     for i in range(len(fullList)):
#         for j in range(len(fullList)-i-1):
#             if fullList[j] > fullList[j+1]:
#                 temp = fullList[j+1]
#                 fullList[j+1] = fullList[j]
#                 fullList[j] = temp
#             print(fullList)
#     return fullList

def bubbleSort(fullList):
    swapped = False
    listLen = len(fullList)
    for i in range(listLen):
        for j in range(listLen - i -1):
            if fullList[j] > fullList[j+1]:
                fullList[j], fullList[j+1] = fullList[j+1], fullList[j]
                swapped = True
        if not swapped:
            break
    return fullList


if __name__ == '__main__':
    fullList = []
    elementsCount = int(input('Enter number of elements: '))
    print('Enter elements: ')
    for i in range(elementsCount):
        element = int(input())
        fullList.append(element)
    # fullList = [12, 7, 19, 3, 15, 17]
    fullList = bubbleSort(fullList)
    print('Sorted list is', fullList)