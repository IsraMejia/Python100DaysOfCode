print('List data structure')

fruits = ['Banana', 'Apple', 'Cherry']

statem1 = 'CDMX'
statem2 = 'Qro'
statem3 = 'Yucatan'

states_mexico = [ statem1 , statem2, ]

print(f' {states_mexico[-2]}') #CDMX

states_mexico.append('Chiapas')

print(states_mexico)

#extend ->  which adds a whole bunch of items
states_mexico.extend(fruits)
print(f'\n\nextend {states_mexico}')

print(f'The numbre of states of Mexico is: {len(states_mexico)}')

fruits2 = ['Strawberries', 'nectarines', 'Apples', 'Grapes', 'peaches' , 'Cherries', 'Pears']
vegetables = {'Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes'}

dirty_dozen = [fruits , fruits2, vegetables] #List of lists
print(f'\nMy list of list: \n {dirty_dozen}')