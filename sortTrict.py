l = [1,4,3,8,10,5,30,6,11]
m = 30


def sorty(l,m):

    l1 = []
    l2 =[]
    for i in range(len(l)):

        if l[i] <= m:
            l1.append(l[i])
        else:
            l2.append(l[i])



    return -1


print sorty(l,m)