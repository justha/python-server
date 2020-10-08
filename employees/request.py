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


    
    