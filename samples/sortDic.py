d = { "a":4, "c":31, "b":12 }
d_view = [ (v,k) for k,v in d.iteritems() ]
d_view.sort(reverse=True) # natively sort tuples by first element
print d_view
for v,k in d_view:
    print "%s: %d" % (k,v)