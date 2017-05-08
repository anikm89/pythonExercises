s = 'AAAABBBBCCCCCDDEEEE'


def compress(s):
    dictChar = {}
    l = []
    for i in range(len(s)):

        if s[i] not in dictChar:
            dictChar[s[i]] = 1
        else:
            dictChar[s[i]] += 1

    for k,v in dictChar.iteritems():
        l.append(k)
        l.append(str(v))


    return "".join(l)



print compress(s)