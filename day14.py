# file handling--creating , opening, reading ,writing and closing
#files types -- .txt, .csv , .json etc
from os.path import exists
'''
"r"-read-file must exists
"w"-write-creates a file, or overwrites a file
"a"-append-adds content to end of file
"x"-create - creates a new file;error if file exists
"r+"-read+write--file mjst exist
"w+"--write+read--overwrites existing file
"a+"--Append+read-- creates file if missing
'''


# A. Reading a file
#1.read entire file
'''f=open("data.txt",'r')
content=f.read()
print(content)
f.close()
'''

#2. Read line by line
'''f=open('data.txt','r')
for line in f:
     print(line)
f.close()'''

#3. read specific nimber of character
'''f=open("data.txt","r")
print(f.read(5))
f.close()'''

#B. wiriting to a file
'''f=open('output.txt','w')
f.write("Hello,Python")
f.close()
'''

#c.Append to a file
'''f=open('output.txt','a')
f.write("\nThis is new content")
f.close()'''


#4. using with--best pratice---with automatically close the file

#with open("info.txt","r") as f :
'''data=f.read()
    print(data)'''

#5
'''f=open("sample.txt","r")
print(f.tell())
print(f.read(5))
f.seek(0)
print(f.read())
f.close()'''

# 6. Exception handling in file I/O
try:
    f=open("unknown.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")