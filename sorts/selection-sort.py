def selectionSort(fullList):
    listLen = len(fullList)
    for i in range(listLen):
        minValueIndex = i
        for j in range(i+1, listLen):
            if fullList[j] < fullList[minValueIndex]:
                minValueIndex = j
        fullList[minValueIndex], fullList[i] = fullList[i], fullList[minValueIndex]
            
        

    return fullList

if __name__ == '__main__':
    fullList = []
    elementsCount = int(input('Enter number of elements: '))
    print('Enter elements: ')
    for i in range(elementsCount):
        element = int(input())
        fullList.append(element)
    # fullList = [12, 7, 19, 3, 15, 17]
    # fullList = [-14,46,43,27,57,41,45,21,70]
    fullList = selectionSort(fullList)
    print('Sorted list is', fullList)