programming_dictionary = {
    "Bug"       : "An error in a program that prevents the program from running as expected. xd", 
    "Function"  : "A piece of code that you can easily call over and over again.",
}

print('\n\tDictionaries\n')

print(programming_dictionary["Bug"]  ) #Retrieving items from dictionary

    # Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing somethin over and over again."
print(f'Dictionary = \n{programming_dictionary}')


empty_dictionary ={}

    #Clear or wipe an existing dictionary
# programming_dictionary = {}
# print(f'Wiped Dictionary = \n{programming_dictionary}')

#Edit an item in dictionary
programming_dictionary['Bug'] = 'Override -> gusano'
print(f'Dictionary = \n{programming_dictionary}')


print('\n\t LOOP through a dictionary')# LOOP through a dictionary
print('Key          \tvalue')
for keyDictionary in programming_dictionary:
    print(f'{keyDictionary}    :  {programming_dictionary[keyDictionary]}') 

#Nesting Dictionaries
print('\n\n\tNesting Dictionaries\n')

capitals = {
    'France'    : 'Paris',
    'Germany'   : 'Berlin'
}

travel_log = {  # Nesting a LIST in a Dictionary
    'France'    : ['Paris',  'Lille', 'Dijon'],         #Key : List
    'Germany'   : ['Berlin', 'Hamburg', 'Stuttgart'],   #Key : List
}

    #Nesting Dictionary in a Dictionary
travel_log = {  # Nesting a LIST in a Dictionary
    'France'    : { 'cities_visited':['Paris',  'Lille', 'Dijon'] , 'total_visits' : 12 } ,  #Key : Dictionary
    'Germany'   : {
        'cities_visited':   ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits' : 21 
    },   #Key : Dictionary
}


    #Nesting a Dictionary in a List
travel_log = [#List   
    { #Dictionary
        'country': 'France',  
        'cities_visited': ['Paris',  'Lille', 'Dijon'] , 
        'total_visits' : 12  
    },

    {#Dictionary
        'country': 'Germany'   , 
        'cities_visited':   ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits' : 21 
    ,}   
]#Nesting a Dictionary in a List

print('\n')

#Quiz, to print 'Steak'
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order['main'][2][0]) #[2] accesses the value with key 2, [0] gets the first item from the list.
