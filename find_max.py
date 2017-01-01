__author__ = 'Murtaza'

def find_max(l):
    max=l[0]

    for i in l:
        if max<i:
            max=i
    return max

res=find_max([31,3,100,121,52,51])
print "The max is:",res