import json

# Define the Employee class
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Define a function to read the employee information from a JSON file
def read_employee_info_from_json_file(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    employees = []
    for employee_data in data:
        employee = Employee(employee_data['name'], employee_data['dob'], employee_data['height'], employee_data['city'], employee_data['state'])
        employees.append(employee)
    return employees

# Define a function to write the Indian states and capitals into a JSON file
def write_indian_states_and_capitals_to_json_file(file_name):
    indian_states_and_capitals = {
        'Andhra Pradesh': 'Amaravati',
        'Assam': 'Dispur',
        'Bihar': 'Patna',
        'Karnataka': 'Bengaluru',
        'Maharashtra': 'Mumbai',
        'Tamil Nadu': 'Chennai',
        'West Bengal': 'Kolkata'
    }
    with open(file_name, 'w') as f:
        json.dump(indian_states_and_capitals, f)

# Read the employee information from the JSON file and print the list of Employee objects
employees = read_employee_info_from_json_file('employee.json')
for employee in employees:
    print(employee.__dict__)

# Write the Indian states and capitals into a JSON file
write_indian_states_and_capitals_to_json_file('indian_states_and_capitals.json')
