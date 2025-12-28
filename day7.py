# List
'''
my_list=["apple","banana","kiwi","orange"]
print(my_list[1])
print(my_list[0])
print(my_list[3])

print(my_list[-2])

my_list[1]="lemon"
print(my_list)'''


# 1.append()

'''fruits=["apple","banana","kiwi","orange"]
fruits.append("grapes")
print(fruits)'''


# 2.insert()

'''fruits=["apple","banana","kiwi","orange"]
fruits.insert(1,'pineapple')
print(fruits)'''


# remove()

'''fruits=["apple","banana","kiwi","orange"]
fruits.remove("apple")
print(fruits)'''



# pop()---remove items by index
'''fruits=["apple","banana","kiwi","orange"]
fruits.pop(0)
print(fruits)

'''

# len()----length of list

'''fruits=["apple","banana","kiwi","orange"]
print(len(fruits))'''


# sort()------sorted list, arranges in ascending order
'''
number=[5,3,8,1]
number.sort()
print(number)
'''


# reverse()
'''number=[1,2,3,4,5,6]
number.reverse()
print(number)'''


# Loop through a list
'''
fruits=['kiwi','banana','mango']

for item in fruits:
    print(item)'''




'''fruits=['kiwi','banana','mango']

if "apple" in fruits:
        print("Apple is present")
else:
        print("You have entered worng fruits name")'''


# 1.Create a list of 5 fruits and print each one using a loop.


'''fruits=['apple','banana','lemon','mango','orange']
for items in fruits:
    print(items)
'''
# 2.Take 5 numbers from user, store in list, print the sum.
'''number=[]
for i in range(5):
    num=int(input("Enter a number:"))
    number.append(num)

print("Your List",number)
print("Sum of numbers:",sum(number)) '''   


# 3.Replace the 3rd item of a list with "Python".
'''lang=["c++","c#","java","kotlin","ruby","react"]
lang.insert(3,"python")
print(lang)'''


# 4.Sort a list of numbers.

''''num=[5,2,7,4,8,1,9]
num.sort()
print(num)'''


# 5. Add "Nepal" to an empty list using append().
'''country=[]
country.append("Nepal")
print(country)'''


# slicing()---extract a part of a list using : symbol
'''num=[10,20,30,40,50]
print(num[1:3])
print(num[2:3])
print(num[0:4])
print(num[:3])
print(num[1:])'''



# List Comprehension---short way to clear list

'''square=[x*x for x in range(1,6)]
print(square)'''


# copy()---copying in a list

'''a=[1,2,3,4]
b=a.copy()
print(b)'''

# clear ---- removes all the items

'''a=[1,2,3,4,5]
a.clear()
print(a)
'''


# extends()----join two list
'''
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
'''

# set


'''my_set={1,2,3}
words={"python","java","c++"}
mixed={10,"hello",3.5}
print(my_set,words,mixed)
'''


# 1. add()


'''s={1,2,3}
s.add(4)
print(s)'''

# 2. update()

'''
s={1,2,3}
s.update([4,5,6,7])
print(s)
'''


# 3. remove
'''s={1,2,3}
s.remove(2)
print(s)'''

# 4. discard()

'''s={1,2,3}
s.discard(10)
print(s)'''


# 5. pop--removes an random items

'''s={1,2,3,4,5,6,7}
s.pop()
print(s)'''


# 6. clear()

'''s={1,2,3}
s.clear()
print(s)
'''

# Set Operation
# 1. union()---combine set
'''a={1,2,3}
b={3,4,5}
print(a.union(b))
'''

# 2. intersection()--common items

'''a={1,2,3}
b={3,4,5}
print(a.intersection(b))'''

# 3. difference---items in a but not in b
'''
a={1,2,3}
b={3,4,5}
print(a.difference(b))
'''

# 4. symmetric_difference()

'''a={1,2,3}
b={3,4,5}
print(a.symmetric_difference(b))'''

# loops through sets

'''names={"ram","sita","hari"}
for n in names:
    print(n)'''



# 1. Create a set of 5 fruits and print each using a loop.
'''fruits=set()
for i in range(6):
    user=input(f"Enter a fruits name{i+1}:")
    fruits.add(user)
print("\nYour fruits are:")
for f in fruits:
     print(f)'''



# 2.      Add a new item to a set using add().

'''a={1,2,3,4,5}
a.add(6)
print(a)
'''

# 3. Remove an item using remove().

'''a={1,2,3,4,5}
a.remove(2)
print(a)'''



# 4. find union andnintersection of two sets

'''a={1,2,3,4,5}
b={4,5,6,7,8,9}
print(a.union(b),"these are union")
print(a.intersection(b),"these are intersection")'''


# 5. Create two sets and find elements only present in the first set.
'''a={1,2,3,4,5}
b={4,5,6,7,8,9}
print(a.difference(b))'''


# frozenset
'''my_frozenset=frozenset([1,2,3])
print(my_frozenset)
'''
