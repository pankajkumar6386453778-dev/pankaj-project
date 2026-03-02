tup = (1 ,2, 3 , 4, 5, "abc" ,3.14)

print(tup)
print(len(tup))

#single value tuple
tup =(1,)

print(type(tup))

#slicing

tup=(1 ,2, 3, 4, 5)

print(tup[0:3])
print(tup[:]) #comple value print


#tuple method

tup =(1 , 2, 3 ,4, 5)

for val in tup:
    print(val) #tuple value

    #sum
    tup = (1,2,3,4,5)

    sum = 0
    for val in tup:
        sum +=val

    print(f"sum of vals is{sum}")

    #tuple method
    tup =(1,2,2,3,2, 4)

    print(tup .index(2)) # 1 out
    print(tup . count(2) )