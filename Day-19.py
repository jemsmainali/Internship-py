#CRUD--create,read,delete,update
  #create
'''from day1 import name

books=[]
  #read
books.append({"id":1,"name":"Sanjay","age":12})
  #update
for b in books:
    if b["id"]==2:
        b["age"]==19
  #delete
books=[b for b in books if b["id"]!=1]
'''


# Bed management in hospital using CRUD functions
'''
bed=[]
def create_bed(type,bed_no):
    bed.append({"type": type, "bed_no": bed_no})

def red_bed():
    for b in bed:
        print(b)

def upadte_bed(type,newbed_no):
    for b in bed:
        if b["type"]==type:
            b["bed_no"]=newbed_no

def delete_bed(type,bed_no):
    global bed
    bed=[b for b in bed if b["type"]!=type]
'''

    #contract management
contract=[]
def create_contract():
    id=int(input("Enter your id:"))
    name=str(input("Enter your name:"))
    email=str(input("Enter your email:"))
    contract.append({"id":id,"name": name, "email": email})
    print("Contract created")

def read_contract():
    if not contract:
        print("No records found")
        return
    for c in contract:
        print(f"ID:{c['id']}|Name:{c['name']}|Email:{c['email']}"   )


def update_contact(name,new_email):
    id=int(input("Enter your id to update:"))
    for c in contract:
        if c["id"]==id:
            c["name"]=input("Enter your name:")
            c["email"]=input("Enter your email:")
            return

    print("Students Not found!")

def delete_contact():
    id=input("Enter your id to delete:")

    global contract
    contact=[c for c in contract if c["id"]!=id]

    print("Successfully deleted")


while True:
    print("\n STUDENT MANAGEMENT SYSTEM ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_contract()
    elif choice == "2":
        read_contract()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")



