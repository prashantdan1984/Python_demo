import json
dict = {
    'Course_name':'Python',
    'fees':15000,
    'duration':'2 month'
}
f=json.dumps(dict)
print(json.dumps(dict))
print(type(json.dumps(dict)))
x=json.loads(f)
print(x)
print(type(x))

for a in x:
    print(a, x[a])
    print(a)

dict1 = [{'id': 1, 'name':'prashant', 'age' : 38, 'work_type' : 'Job'}, 
         {'id': 2, 'name':'bhavna', 'age' : 38, 'work_type' : 'house wife'},
         {'id': 3, 'name':'tanvi', 'age' : 11, 'work_type' : 'student'},
         {'id': 4, 'name':'hetvi', 'age' : 8, 'work_type' : 'student'},
         {'id': 5, 'name':'shauryaveer', 'age' : 5, 'work_type' : 'student'},
         {'id': 6, 'name':'hershdan', 'age' : 66, 'work_type' : 'business'}]

# Create File.

# Create and write file
file=open("json_file.txt", 'w')
file.write(json.dumps(dict1))

file.close()

# Read file.
file=open("json_file.txt", 'r')
y=file.read()
finaldata= json.loads(y)
print(y)
print(type(y))
for a in finaldata:
    print(a['id'], a['name'])

# Append File.
file=open("json_file.txt", 'w')
print(type(finaldata))
finaldata.append({'id': 7, 'name':'shakti', 'age' : 33, 'work_type' : 'job'})
file.write(json.dumps(finaldata))
file.close()

'''
# Append File.
with open("json_file.txt", 'w') as ft:
    listObj=json.loads(ft)
    
#verify existing list
print(listObj)
print(type(listObj))

listObj.append({'id': 7, 'name':'shakti', 'age' : 33, 'work_type' : 'job'})

    #verify updated list
print(listObj)


file =open("json_file.txt", 'w')
xx= {'id': 7, 'name':'shakti', 'age' : 33, 'work_type' : 'job'}
file.write(json.dumps(xx))
file.close()'''

