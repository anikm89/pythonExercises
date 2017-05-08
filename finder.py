
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]


def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            return arr1[i]

    return 0

def finder2(arr1,arr2):

    dictA={}

    for i in range(len(arr2)):
        if arr2[i] not in dictA:
            dictA[arr2[i]] = 1
        else:
            dictA[arr2[i]] += 1

    for i in range(len(arr1)):
        if arr1[i] not in dictA.keys():
            return arr1[i]

    return 0



print finder2(arr1,arr2)