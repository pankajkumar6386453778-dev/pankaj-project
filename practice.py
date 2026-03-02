info =[
    ("alice","math"),
    ("bob","science"),
    ("alice","science"),
    ("charlie","math"),
    ("bob","math"),
    ("alice","english"),
    ("charlie","english"),
]
unique_courses = set()
for tup in info:
    unique_courses .add(tup[1])
print(unique_courses)  
   # print(tup[0])#name
   
   # print(tup[1]) #suj

for name,course in info:
    if(course == "english"):
        print(name)

dict ={}

for name,course in info:
    if(dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add (course)
else:
    dict[name].add(course) 

print(dict)         
