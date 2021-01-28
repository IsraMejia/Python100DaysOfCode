import random

names = input("Give me everybody's names, separated by a comma. ").split(", ") #split the string in substrings into a list

print(f"My friends in the dinner are : {names}")

num_friends = len(names) 
indexfriend = random.randint (0 , num_friends -1)
print(f"{names[indexfriend]} is going to buy the meal today! jaja ")