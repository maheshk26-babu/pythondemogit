"""
Else block will execute if condition does not meet otherwise it skip if it meets condition(break the loop)
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in l1:
    if x == 8:
        break
    print(x, end=' ')
else:
    print("\nElse block executed")
print("\nOut of for loop")
print("********************************")

price=400
cost= 'Expensive' if price > 500 else 'Low_medium'
print(cost)
a=10
b=20
max = a if a>b else b
print(max)
print("********************************")

