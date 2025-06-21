#!/usr/bin/env python3

def array_of_names(my_dict):
    arr = []
    for key,value in my_dict.items():
        arr.append(f"{key.capitalize()} {value.capitalize()}")
    return arr

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))