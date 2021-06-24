# A list is mutable, we can change the value of any index element at runtime
list1= [10, 'A', 'python', 12.56, True]
print(list1)

list2= [10, 20, [1, 2, 3], 'python', False]
print(list2)
print(list2[0])
print(list2[2])
print(len(list2))
print(list2[-1])
print(list2[1:3])

list2[4] = 'India'
print(list2)

del list2[2]
print(list2)
del list2[1:3]
print(list2)
del list2
# print(list2)

l1= [8,5,3,2]
l2= [1,5,9]
l1.append(l2) #### [8,5,3,2,[1,5,9]]
# print(l2)
l1.extend(l2) ### [8,5,3,2,1,5,9]
print(l1)


l1 = ['aa', 'bc', 'ab', 'aa', 'cd', 'bc', 'aa', 'bc']
for l in l1:
    print(l)

out = set(l1)
print("List without duplicate items using 'Set' data type :", list(out))

l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print("List without duplicate items :", l2)

print("'{}' occurred {} times in list" .format('bc', l1.count('bc')))
count = 0
for i in l1:
    if i == 'aa':
        count += 1
print("'aa' occurred {} times".format(count))

# l1=['aa', 'bc', 'ab', 'aa', 'cd', 'bc', 'aa', 'cd']
l1 = ["python", "java", "selenium", "python", "JS", "python", "JS"]
l2 = []
count = 1
for i in range(0, len(l1)):
    if l1[i] not in l2:
        l2.append(l1[i])
        for j in range(i + 1, len(l1)):
            if l1[i] == l1[j]:
                count += 1
        print("count of {} is {}".format(l1[i], count))
        count = 1

l1 = ['aa', 'bc', 'ab', 'aa', 'cd', 'bc', 'aa']
print([(x, l1.count(x)) for x in set(l1)])

for i,j in enumerate(set(l1)):
    print(i,j)

l3 = []
for j in l1:
    l3.append(j)
print(l3)

out = [j for j in l1]
print(out)


l1= [1,2,3,2,8,4]
l2= [4,5,6]
l3= ['Mahesh',23, 5.5]
l4='Babu'
# l4= 23
# l4= [23]
# l4= 'Python is a programming language'
# l4= True
print(l1.count(4))
print(l1.index(2))
l1.append(l4)
l1.append(l2[2])
print(l1)
l1.extend(l4)
print(l1)
it=iter(l4)
print(next(it))
print(l1.count(2))
l5= l1.copy()
print(l5)
print(l1.index(8))
# print(l1.clear())
l1.remove(4)
print(l1)
l1.insert(3, 10)
print(l1)
l1.reverse()
print(l1)
# l1.sort()
print(l1)
l9= [3,5,7,2,9,6,1,5]
l9.sort()
print(l9)
print(len(l1))
if 'Babu' in l1:
    print("exists")

l1 = ['apple', 'cherry', 'banana', 'berry', 'almond']
# l1 = [5, 3, 7, 2, 6, 11, 24, 17]
print(sorted(l1))
print(sorted(l1, reverse=True))
reversed_list = list(reversed(l1))
print(reversed_list)
print(l1[::-1])

for i in range(len(l1)-1):
    for j in range(i+1, len(l1)):
        if l1[i] <= l1[j]:
            temp = l1[i]
        else:
            temp = l1[j]
            l1[j] = l1[i]
            l1[i] = temp
print(l1)


