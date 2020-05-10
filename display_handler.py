def display_definition_list(definition_list):
    if len(definition_list) == 1:
        print('\nDefinition:')
        print(definition_list[0])
    else:
        for i in range(len(definition_list)):
            print(f'\nDefinition {i + 1}:')
            print(definition_list[i])


def display_results(result):
    if type(result) == list:
        display_definition_list(result)
    else:
        print(result)