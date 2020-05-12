def mergeSort(fullList):
    if len(fullList) > 1:
        # find the mid
        mid = len(fullList)//2

        # prepare 2 lists
        leftList = fullList[:mid]
        rightList = fullList[mid:]
        print('mid left right', mid, leftList, rightList)

        # sort these list recursively
        mergeSort(leftList)
        mergeSort(rightList)

        i = j = k = 0
        print('merging')
        # compare elements
        while i < len(leftList) and j < len(rightList):
            print('sort left right full', leftList, rightList, fullList)
            if leftList[i] < rightList[j]:
                fullList[k] = leftList[i]
                i += 1
            else:
                fullList[k] = rightList[j]
                j += 1
            k += 1

        # if any element left in left list
        while i < len(leftList):
            fullList[k] = leftList[i]
            i += 1
            k += 1

        # if any element right in left list
        while j < len(rightList):
            fullList[k] = rightList[j]
            j += 1
            k += 1

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
    fullList = mergeSort(fullList)
    print('Sorted list is', fullList)