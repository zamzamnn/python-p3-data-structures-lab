spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass

def get_spiciest_foods(spicy_foods):
    pass

def print_spicy_foods(spicy_foods):
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass







# questions solved in the lab
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# Test
print(get_names(spicy_foods))
# Output: ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

# def get_spiciest_foods(spicy_foods):
#     return [food for food in spicy_foods if food["heat_level"] < 5]
#     print(get_spiciest_foods(spicy_foods))


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# Test
print(get_spiciest_foods(spicy_foods))
# Output: [{"name": "Green Curry", ...}, {"name": "Mapo Tofu", ...}]



def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')




def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

# Test
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
# Output: {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}



def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

# Test
print_spiciest_foods(spicy_foods)



def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

# Test
print(get_average_heat_level(spicy_foods))
# Output: 6



def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods

# Test
new_food = {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}
print(create_spicy_food(spicy_foods, new_food))








