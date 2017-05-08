
import timeit
s = 'tree traversal'

def dups(s):
     newS = []
     d ={}

     for i in range(len(s)):
         if s[i] not in newS:
             newS.append(s[i])
     return "".join(newS)


def unique(s):
   result =[]
   seen ={}

   for item in s:
       if item not in seen:
           seen[item] = 1
           result.append(item)
   return "".join(result)

t = timeit.Timer("print 'main statement'", "print 'setup'")

print t(unique(s))
print dups(s)