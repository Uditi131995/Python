# I wake up
# If I am hungry
#     I eat breakfast

# I leave my house
# if its cloudy
#     I bring an umbrella
# otherwise
#     I bring sunglasses


# I am at a restaurant
# if I want meat
#     I order a steak
# otherwise if I want pasta
#     I order spaghetti & meatballs
# otherwise
#     I order a salad


is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("you are neither male or tall")

# nested if
if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not is_tall:
    print("You are a short male")
else:
    print("you are neither male or tall")
