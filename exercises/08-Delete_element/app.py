people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
   # return 
    
    new_list =[]
    for name in people:
        if name != person_name:
            new_list.append(name)
    return new_list

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))