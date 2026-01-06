 # 1. Write a program to create a file and write your name in it.
'''filename='my_file.txt'
name="Nischal Mainali"

with open(filename,"w")as f:
    f.write(name)

print(f"Successfully created '{filename}'and wrote '{name}' to it")    
'''

 # 2. Read a file and display its content
'''with open("my_file.txt", "r") as f:
    print(f.read())
 '''
# 3. Append data to an existing file
'''
with open ("my_file.txt","a") as f:
    text="Ronaldo"
    f.write(text)
    print(text)
 '''


# 4. count number of character in a line
'''with open ("my_file.txt","r") as f:
    for line in f:
        print(line)
    print(len(line))
    '''

# 5. count number of lines in a file

'''with open("my_file.txt","r") as f:
    lines=f.readlines()

    print(len(lines))'''

#6.Read a file and print only lines that start with a vowel.
'''with open("coding.txt", "r") as f:
    for line in f:
        if line and line[0].lower() in 'aeiou':
            print(line, end="")

'''
# 7. Read numbers from a file and print their sum.
'''total=0
with open("coding.txt","r") as f:
    for line in f:
        total+=int(line.strip())

    print(total)
'''

#Copy content from one file to another.
'''import shutil
src="source.bin"
dstn="destination.bin"
with open("src","wb") as f:
    f.write(b"Binary data examples")

with open("dstn","rb") as fsrc,open(dstn,"wb") as fdstn:

    shutil.copyfileobj(fsrc,fdstn)

print(f"content of file copied form '{src}' to '{dstn}'")
'''

#Write multiple lines using writelines().
lines=["Apple\n","Banana\n","orange\n"]
with open("coding.txt","w")as f:
    f.writelines(lines)

print("Lines successfully written to coding.txt")