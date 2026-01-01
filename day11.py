#iterator
#eg
'''my_list=[4,2,7,8]
iterator=iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
'''

'''my_list=[4,2,7,8]

for element in my_list:
    print(element)'''


# loop in iterator
'''my_list=[4,2,7,8]
iterator=iter(my_list)

for element in iterator:
    print(element)'''


#building a custom iterator

class Powtow:


    def __init__(self, max=0):
      self.max=max

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<=self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration



number= Powtow(3)
i=iter(number)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

