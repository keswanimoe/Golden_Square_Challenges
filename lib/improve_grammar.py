def improve_grammar(text):
# Parameters: text: a string 
# Returns: True or False
# Side effects: no side effects, nothing is printed
    check = set('!.,')
    if any((sp in check) for sp in text[-1]) and text[0].isupper() == True:
        return True
    else:
        return False
