nums =[1,2,3,10,4]

for val in nums:
    print(val)

    #uedd find val help of index

    nums=[1,2,3,10,4]

    x=10
    idx=0

    for val in nums:
        if(val  == x):
            print( f"{x} found at idx ={idx}")
            break
        idx +=1
