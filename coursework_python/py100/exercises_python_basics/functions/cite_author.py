def bruce_eckel_quote():
    print('Python is executable pseudocode.')

def cite(author, quote):
    print(f'{author} said: "{quote}"')

cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

def cite(author, quote):
    print('{} said: "{}"'.format(author, quote))
