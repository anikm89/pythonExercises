
s1 = "clint eastwood"
s2 = "old west action"


def anagram(s1,s2):
    result =''
    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")

    dictS1 = {}
    if len(s1) !=len(s2):
        return False


    for i in range (len(s1)):
        if s1[i] not in dictS1:
            dictS1[s1[i]] = 1
        else:
            dictS1[s1[i]] += 1


    for i in range (len(s2)):
        if s2[i] in dictS1:
            dictS1[s2[i]] -= 1
        else:
            dictS1[s2[i]] = 1

    for k in dictS1.keys():
        if dictS1[k]!=0:
            return False

    return True

    """
    for i in range (len(s2)):
        if s2[i] not in dictS2:
            dictS2[s2[i]] = 1
        else:
            dictS2[s2[i]] += 1


    if (dictS1.keys()==dictS2.keys()) and (dictS1.values()==dictS2.values()):
        return True

    else:
        return False
    """


def anagram2(s1,s2):

    s1 = list(s1.replace(" ","").lower())
    s2 = list(s2.replace(" ","").lower())
    (s1).sort()
    (s2).sort()
    result = ''

    if len(s1) !=len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
        else:
            result =True


    return result


print anagram(s1,s2)