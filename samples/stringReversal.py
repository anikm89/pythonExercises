

s = '       This is the best        '


def rev_word(s):
    s = s.strip().lstrip().split(" ")
    r = []
    print s

    for i in range((len(s))):
        r.append(s[-(i+1)])
    return " ".join(r)



print rev_word(s)