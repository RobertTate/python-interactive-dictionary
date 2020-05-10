from difflib import get_close_matches

def normalize(w):
    return w.lower()

def handle_suggestion(w, data):
    suggestion = get_close_matches(w, data.keys())[0]
    response = ''
    while response != 'y' and response != 'n':
        print(f'Did you mean {suggestion}?')
        response = normalize(input('(Y or N)'))
    if response == 'y':
        return data.get(suggestion)
    else:
        return 'Sorry, no other suggestions found.'


def find_definition(w, data):
    w = normalize(w)
    if data.get(w):
        return data.get(w)
    elif get_close_matches(w, data.keys()):
        return handle_suggestion(w, data)
    else:
        return 'No definition found.'
