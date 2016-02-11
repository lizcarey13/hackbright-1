# Given a food tuple, where all the odd positions are the names of the food, 
# and all the even positions are the corresponding prices, i.e.:
food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99)

# Write a function to convert the food tuple into a food dictionary where we 
# can use food name as key to access its price, i.e.:
# > print food_dictionary['sushi']
# > 7.50

def convert_tuple_to_dict(tuple) :
    item_index = 0
    food_dictionary = {}
    for item in tuple:
        # if item is in position 0, 2, 4, ...., it is the food name
        if item_index % 2 == 0 :
            food_dictionary[item] = tuple[item_index + 1]
        item_index += 1

    return food_dictionary

food_dictionary = convert_tuple_to_dict(food_price_tuple)
print food_dictionary
print food_dictionary['sushi']



