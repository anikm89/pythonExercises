
l = [1,-1,1,-1,4,-4,1,-10,-1,50,100]
#l =[-1,1]

def large_cont_sum2(arr):


    if len(arr)==0:
        return 0

    max_sum=current_sum=arr[0]
    print arr[1:]

    for num in arr[1:]:

        current_sum=current_sum+num
        if num > current_sum:
            current_sum = num

        if current_sum > max_sum:
            max_sum= current_sum


    return max_sum

print large_cont_sum2(l)