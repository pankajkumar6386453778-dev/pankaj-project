s = {1,2,2,2,3}

empty_set = set() #used to print empty set

print(type(empty_set))

s.add(5)
s.remove(1) #used remove to any element
s.clear()


print(s)

#pop

s= {1,2,2,2,3}
print(s)
s.pop()
print(s)

#union
s1 ={1,2,3,4,5}
s2 = {4,5,8,9,10}

print(s1.union(s2))
print(s1.intersection(s2))

