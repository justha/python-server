EMPLOYEES = [
    {
        "id": 1,
        "name": "Sia",
        "locationId": 1,
        "animalId": 1
    },
    {
        "id": 2,
        "name": "Willy Wonka",
        "locationId": 1,
        "animalId": 2
    },
    {
        "id": 3,
        "name": "Charlie Bucket",
        "locationId": 2,
        "animalId": 3
    }
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee
    
    
def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
    
    