# Recursion Method
# def binarySearch(fullList, start, end, number):
#     if end > start:
#         mid = start + (end - start) // 2
#         middleElement = fullList[mid]
#         if middleElement == number:
#             return mid
#         elif middleElement < number:
#             start = mid + 1
#             return binarySearch(fullList, start, end, number)
#         else:
#             end = mid - 1
#             return binarySearch(fullList, start, end, number)
#     else:
#         return -1

# Iteration method
def binarySearch(fullList, start, end, number):
    while end > start:
        mid = start + (end - start) // 2
        middleElement = fullList[mid]
        if middleElement == number:
            return mid
        elif middleElement < number:
            start = mid + 1
        else:
            end = mid - 1
    else:
        return -1


if __name__ == '__main__':
    # aList = [1, 7, 9, 20, 40, 80, 87, 93, 102, 117]
    aList = []
    elementsCount = int(input('Enter number of elements: '))
    print('Enter elements')
    for i in range(elementsCount):
        element = int(input())
        aList.append(element)
    searchElement = int(input('Search for element: '))
    index = binarySearch(aList, 0, len(aList)-1, searchElement)
    if index == -1:
        print('Element not found.')
    else:
        print('index of element', index)