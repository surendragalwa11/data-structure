def insertionSort(fullList):
    listLen = len(fullList)
    for i in range(1, listLen):
        keyVal = fullList[i]
        j = i-1
        while j >= 0 and keyVal < fullList[j]:
            fullList[j+1] = fullList[j]
            fullList[j] = keyVal
            j -= 1
            
        

    return fullList

if __name__ == '__main__':
    fullList = []
    elementsCount = int(input('Enter number of elements: '))
    print('Enter elements: ')
    for i in range(elementsCount):
        element = int(input())
        fullList.append(element)
    # fullList = [12, 7, 19, 3, 15, 17]
    # fullList = [14,46,43,27,57,41,45,21,70]
    fullList = insertionSort(fullList)
    print('Sorted list is', fullList)