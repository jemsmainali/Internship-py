# working with CSV files -- comma-separate values(excel like data)
'''import csv
with open('data.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
'''
# use next(reader) to skip the header
'''import csv
with open('data.csv','r')as file:
    reader= csv.reader(file)
    next(reader)
    for row in reader:
        print(row)'''

# ii. reading CSV as dictionary
'''import csv
with open('data.csv','r')as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)
'''
# iii. writing to a CSV file
'''import csv
data=[
    ["name","age",'city'],
    ["ram","23",'lalbandi'],
    ["shyam","20",'birjung']
]
with open('new_data.csv','w',newline="")as file:
    writer=csv.writer(file)
    writer.writerows(data)
    '''

#iv. Writing CSV as dictionary
'''import csv
data = [
    {'name': 'Hari', 'age': 21, 'city': 'Bhaktapur'},
    {'name': 'Gita', 'age': 22, 'city': 'Kathmandu'}
]
with open('new_data.csv','w',newline='')as file:
    filedname=["name","age","city"]
    writer=csv.DictWriter(file,fieldnames=filedname)

    writer.writeheader()
    writer.writerows(data)
'''
#using pandas libary
import pandas as pd
df=pd.read_csv('data.csv')
print(df)