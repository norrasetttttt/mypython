a = {1,2,3,4,5,6,7,13}
b = {1,3,5,13,14}
c = {5,8,9,12}
print(a.union(b).union(c))
print(a | b | c)

print(a.intersection(b).intersection(c))
print(a & b & c)
        
print(b.difference(a).difference(c))
#print(a - b - c)