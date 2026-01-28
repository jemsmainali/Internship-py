# Write a program to display “MDS” 10 times.

#Answer1
for i in range(1,11):
    print("MDS")


#Answer2
j = 0
while j < 10:
    print("MDS")
    j += 1


#Answer3
def mds_print(times):
    for _ in range(times):
        print("MDS")

mds_print(10)