
#l = [1,3,5,6,7,2,2]
#t = 4
l =[4,2,3]
t = 6
def pair_sum(l,t):
    length = len(l)
    result = []
    for index1 in range(len(l)-1):
        index2 = index1+1
        while index2 < len(l):
            sum = l[index1]+l[index2]
            if sum == t:
               result.append((l[index1],l[index2]))
            index2 = index2+1
    return (result), len(result)


def pair_sum2(arr,target):

    if len(arr)<2:
        return

    # Sets for tracking
    seen = set()
    output = set()
    output2 = set()

    # For every number in array
    for num in arr:

        # Set target difference
        diff = target-num

        # Add it to set if target hasn't been seen
        if diff not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            v = num
            y = diff
            a = (num,diff)
            output.add(a)

    return list(output)

print pair_sum2(l,t)
print pair_sum(l,t)