LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "1000 Main Street"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "2000 Main Street"
    }
]


def get_all_locations():
    return LOCATIONS


def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location


def create_location(location):
    max_id = LOCATIONS[-1]["id"]

    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location
    
    
def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break    
    