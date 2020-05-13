def partition(partialList, low, high):
    i = low - 1
    pivot = partialList[high]
    for j in range(low, high):
        if partialList[j] < pivot:
            i += 1
            partialList[i], partialList[j] = partialList[j], partialList[i]
    partialList[i+1], partialList[high] = partialList[high], partialList[i+1]
    return i+1

def quickSort(fullList, low, high):
    if low < high:
        # partition the array
        p = partition(fullList, low, high)

        # sort the partitioned array
        quickSort(fullList, low, p-1)
        quickSort(fullList, p+1, high)
        print(fullList)
    return fullList





if __name__ == '__main__':
    fullList = []
    # elementsCount = int(input('Enter number of elements: '))
    # print('Enter elements: ')
    # for i in range(elementsCount):
    #     element = int(input())
    #     fullList.append(element)
    # fullList = [12, 7, 19, 3, 15, 17]
    fullList = [14,46, -43,27,57,41,45,21,70]
    fullList = quickSort(fullList, 0, len(fullList)-1)
    print('Sorted list is', fullList)