def format_name(first_name , last_name):
    """Docstring: Take a first an last name and format it to return the title case version of the name 
     this we can see when we put the mouse into the code function 👀"""
    name = first_name + ' ' + last_name
    return name.title() #title to convert in capital caracter just the first caractar per word

print(format_name(first_name = 'isra', last_name = 'mejia'))
