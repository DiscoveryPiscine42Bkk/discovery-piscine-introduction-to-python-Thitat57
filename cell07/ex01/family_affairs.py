#!/usr/bin/env python3

def find_the_redheads(my_dict):
    return (list(filter(lambda key: my_dict[key] == "red", my_dict)))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))