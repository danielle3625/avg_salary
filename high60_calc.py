import csv
import re


# open the file
data = open('export_ledge_noedits.CSV')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

# get parish name
# for this example file, only need to input 'East'
parish = input("Please Enter Parish Name: ")

# setup empty lists to get salary
parish_salary = {}
state_salary = {}
combined_salary = {}

#period_ends = []
#parish_salary_values = []


for line in data_lines:
    for item in line:
        if line[0].startswith('Employer') or line[0].startswith(parish):
            #period_ends.append(line[2])
            #parish_salary_values.append(line[4])
            parish_salary[line[2]] = line[4]
        if line[0].startswith('State'):
            state_salary[line[2]] = line[4]

for item in parish_salary:
    for key, value in parish_salary.items():
        value = value.replace(',','')
        parish_salary[key] = value

for item in state_salary:
    for key, value in state_salary.items():
        value = value.replace(',','')
        state_salary[key] = value


for k,v in parish_salary.items():
     print(f'Parish {k} {v}')
     
for k,v in state_salary.items():
    print(f'State {k} {v}')

for k,v in parish_salary.items():
    for key,value in state_salary.items():
        if k == key:
            combined_salary[k] = float(v) + float(value)

for k,v in combined_salary.items():
    print(f'Combined {k} {v: .2f}')