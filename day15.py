#working with JSON files
#JSON(javascript object notation)
# reading to JSON file (using json.load()--loads json content from json file into a dictionary
'''import json
with open("data.json","r")as f:
    data=json.load(f)
print(data)
print(type(data))
'''
from xml.etree.ElementTree import indent

from day1 import name

#using json.loads()--used to prase json string to convert into a python object
# Example: Convert a JSON-formatted string into a Python dictionary.

'''import json
json_str='{"name":"rodrygoes","club":"real-madrid"}'
data=json.loads(json_str)
print(data)
print(type(data))
'''


# 1. using json.dumps()
'''import json
data={
    "name":"Banset Babu",
    "age":12,
    "CGPA":3.99,
    "Loaction":"Kathmandu"
}
json_str=json.dumps(data , indent=4)
with open('data.json','w')as f:
    f.write(json_str)

    print(json_str)
'''

# 2. using json.dump()--directly writes the dictionary to a file in the form of json without needing to convert in to a actual JSON format
'''import json
data={
    "name": "Banset Babu",
    "age": 12,
    "CGPA": 3.99,
    "Loaction": "Kathmandu"
}
with open('data.json','w')as d:
    json.dump(data,d)
'''
#Create a dictionary with your:
'''import json
data={
    "name":"Jems Mainali",
    "age":22,
    "city":"kathmandu"
}
with open("profile.json","w") as f:
    json.dump(data,f)

print(data)
print(type(data))'''

# Write a dictionary containing:product_name,price,quantity,Store it in product.json using json.dump()

'''import json
data={
    "product_name":"facewash",
    "price":213,
    "quantity":2

}
with open("product.json",'w')as f:
    json.dump(data,f)

'''
# Write a list of numbers [10, 20, 30, 40] into a JSON file called numbers.json.
'''import json
data=[10,20,30,40]
with open('number.json','w')as f:
    json.dump(data,f)'''

# Read the file profile.json and print only the name.
'''import json
with open("profile.json","r")as f:
    data=json.load(f)
    print(data["name"])
   '''

 # read product.json and calculate total_price  and pint the result

'''import json
with open("product.json","r")as f:
     data = json.load(f)
     price=data["price"]
     quantity=data["quantity"]
     total_price=price*quantity
print(total_price)
'''

# Read numbers.json and print the sum of all numbers.
'''import json
with open("number.json","r")as f:
    data=json.load(f)
    total=sum(data)
    print(total)'''

