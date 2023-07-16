set={1,2,3,4,5,6}


set.add(9)
print(set)

set.discard(3)
print(set)


set1={1,3,2,4,5,6}
set2={5,6,7,8,9}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

#if a element is present in set

s={1,2,3,4,5,6,7,8}
if 2 in s:
    print("is present")
else:
    print("not present")


#print all elements
s={1,2,3,4,5,6,7,8}
for i in s:
    print(i)




