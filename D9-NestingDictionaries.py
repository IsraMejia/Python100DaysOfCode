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