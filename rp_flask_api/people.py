# people.py

from datetime import datetime

#this function generates a string representation of the current timestamp
def get_timestamp():

    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# We define the people dictionary data stucture
PEOPLE = {

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