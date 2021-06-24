# Strings are immutable, they cannot be changed. You cannot change any character within it
import re

str = 'python'
print(str[1])
print(str[3])
# print(str[6])

print(str[2:5])
print(str[::])
print(str[1:])
print(str[:1])
print(str[::-1])
print(str[:-3])
print(str[-4])

# str[3]='j'
# print(str)

str = 'DevOps'
print(str)

s1 = "Automation Testing"
print(s1)
del s1
# print(s1)

s2 = "I\'m \tAutomation Test Engineer\nPython"
print(s2)

print("/\"Hello/\"")
print("/'Hello'/")
print("\"/'Hello'/\"")
print("I love \"python\" and \"programming\" and \"movies\"")
print("'I love \"python\" and \"programming\" and \"movies\"'")


str1 = "python is a programming language python"
str2 = ''
for i in str1:
    if i not in str2:
        str2 = str2 + i
print("String without duplicate characters:", str2)
print("length of the string:", len(str1))
print("'{}' character occurred {} times in string".format('t', str1.count('t')))

str1 = "python is a programming language python java python language"
str2 = ''
count = 1
# print(len(str1))
for i in range(0, len(str1)):
    if str1[i] not in str2:
        str2 = str2 + str1[i]
        for j in range(i + 1, len(str1)):
            if str1[i] == str1[j]:
                count += 1
        print("count of {} is {}".format(str1[i], count))
        count = 1

sub_str = 'python'
print(str1.count(sub_str))
matches = re.finditer(sub_str, str1)
matches_positions = [match.start() for match in matches]
print("sub_string position in string:", matches_positions)


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
        print(string[i:i + len(sub_string)])
    return count


print("sub_string count:", count_substring(str1, sub_str))

str = "malayalam"
if str == str[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")

out1='-'.join(['a', 'bc', 'cd'])
print(out1)
str3= 'python is a \nprogramming \tlanuguage'
print(str3.split('_'))
print(''.join(reversed(str3)))
print('-'.join(['p', 'y', 't', 'h', 'o', 'n']))
animal = 'fish'
print(animal[0].upper()+animal[1:3]+animal[-1].upper())
print(str3.splitlines())
print(str3.replace('python', 'java'))
print(min(animal))
string = '  string of whitespace    '
print(string.lstrip())
print(string.rstrip())
print(string.strip())

city = 'New York'
print(city.startswith('N',0))
print(city.endswith('N',0))
print(''.isspace())
print(' '.isspace())
print('aha'*3)
print(str3.title())
sentence = "If you want to be a ninja"
print(sentence.partition('to'))
animal = 'dog'
print(id(animal))

pet = 'dog'
print(id(pet))

# create mapping
mapping = str.maketrans("abct", "123S")
# translate string
print("abc are the first three letters".translate(mapping))
#=> '123 1re the firSt three letterS'


file_name = 'sales_2021.xlsx'
month_and_extension = file_name.split('_')[1]
print(month_and_extension)
month_name = month_and_extension.split('.')[0]
print(month_name)

# print i am a boy
# boy a am i
str1 = 'i am a boy'
str2 = ''
res = str1.split(' ')
for i in range((len(res)-1), -1, -1):
    str2 = str2 + res[i] + ' '
print(str2)