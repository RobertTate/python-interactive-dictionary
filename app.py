from definition_handler import find_definition
from display_handler import display_results
import json


with open('data.json', 'r') as json_file:
    data = json.load(json_file)

word = input("Enter word to lookup: ")

definition = find_definition(word, data)

display_results(definition)