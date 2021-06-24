# Dictionary is mutable, we can change the value of any key
# Elements of dictionary are not arranged in orderly fashion. Thus you cannot access a specific element using
# its index. We can access a specific element of a dictionary using its key

dict1 = {"Name": "Mahesh", "age": 30, 1:"emp1", 2:True}
print(dict1)

dict2 = {'QA': 'Python', 'Total': 3}
print(dict2)
print(dict2['Total'])
print(dict2.get('QA'))
# print(dict2['name'])
print(dict2.get('name'))
dict2['QA']='Jenkins'
print(dict2)

if 'QA' in dict2:
    print(dict2['QA'])


employee = {"id":"09", "name": "Nitin", "department":"Finance", "id":"35"}
print(employee.keys())
print(employee.values())
print(employee.items())
print(employee.get('id'))
print(employee.get('Number'))
# print(employee.clear())
emp1=employee.copy()
print(emp1)
employee['id']=456
print(employee)

dict3 = {'K': "Mahesh", 'Age': 30}
output = '-'.join(dict3)
print(output)
print(type(output))


dictlang = {'C#': 6, 'GO': 89, 'Python': 4, 'Rust': 10}
# print(dictlang['C#', 'GO'])

total={}
def insert(items):
    if items in total:
        total[items] += 1
    else:
        total[items] = 1
insert('Apple')
insert('Banana')
insert('Apple')
print(total)
