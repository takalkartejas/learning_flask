# people.py

from datetime import datetime
from flask import abort

#this function generates a string representation of the current timestamp
def get_timestamp():

    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# We define the people dictionary data stucture
PEOPLE = {
    # the last name is used as key as you can see
    "Fairy": {

        "fname": "Tooth",

        "lname": "Fairy",

        "timestamp": get_timestamp(),

    },

    "Ruprecht": {

        "fname": "Knecht",

        "lname": "Ruprecht",

        "timestamp": get_timestamp(),

    },

    "Bunny": {

        "fname": "Easter",

        "lname": "Bunny",

        "timestamp": get_timestamp(),

    }

}

# this is the function called in swagger.yml operationID for get
def read_all():

    return list(PEOPLE.values())


def create(person):

    lname = person.get("lname")

    fname = person.get("fname", "")

# if the lastname exists and it is not already in the list
    if lname and lname not in PEOPLE:

        PEOPLE[lname] = {

            "lname": lname,

            "fname": fname,

            "timestamp": get_timestamp(),

        }

        return PEOPLE[lname], 201

    else:
# abort funtion used to send the error response
        abort(

            406,

            f"Person with last name {lname} already exists",

        )

def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )

 #Note: A person’s last name must be unique, because you’re using lname
 # as a dictionary key of PEOPLE. That means you can’t have two people 
 # with the same last name in your project for now.


# this method only changes the first name and time
def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404,
            f"Person with last name {lname} not found"
        )