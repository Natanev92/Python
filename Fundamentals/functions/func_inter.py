x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Update values in dictionaries and lists
def update_nums(list):
    list[1][0] = 15
    return list

update_nums(x)

def change_last_name(students):
    students[0]['last_name'] = "Bryant"
    return students

change_last_name(students)

def update_sports_directory(directory):
    directory["soccer"][0] = "Andres"
    return directory

update_sports_directory(sports_directory)

def modify_value(values):
    values[0]["y"] = 30
    return values

modify_value(z)

# Iterate through a list of dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
    ]

def iterate_dictionary(some_list):
    for i in some_list:
        print("first-name -", i['first_name']+ ", last_name -", i['last_name'])

iterate_dictionary(students)

# Get values from a list of dictionaries
def iterate_dictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

# Iterate through a dictionary with list values
def print_info(some_dict):
    for keys in some_dict:
        print(len(some_dict[keys]), keys.upper())
        for values in some_dict[keys]:
            print(values)
        print("\n")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print_info(dojo)