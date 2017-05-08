l =[1,2,3]

def sq(l):

    #l = [i*i for i in l]

    l = map(lambda x:(1,x),l)
    return l


print sq(l)