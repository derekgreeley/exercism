"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):

    if any(ingredient in ALCOHOLS for ingredient in drink_ingredients):
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"



def categorize_dish(dish_name, dish_ingredients):
    categories = {
        "VEGAN": VEGAN ,
        "VEGETARIAN": VEGETARIAN ,
        "PALEO": PALEO,
        "KETO": KETO,
        "OMNIVORE": OMNIVORE,
    }

    for category, allowed_ingredients in categories.items():
        if dish_ingredients <= allowed_ingredients:
            return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    dish_name, ingredients = (dish)
    special_tags = set(ingredients) & SPECIAL_INGREDIENTS
    return (dish_name, special_tags)



def compile_ingredients(dishes):
    master_list= set()
    for dish in dishes:
        master_list.update(dish)
    return master_list


def separate_appetizers(dishes, appetizers):
    unique_apps = set(appetizers)
    seen = set()
    result = []
    for dish in dishes:
        if dish not in unique_apps and dish not in seen:
            result.append(dish)
            seen.add(dish)

    return result
    

def singleton_ingredients(dishes, intersection):
    all_ingredients = set().union(*dishes)
    return all_ingredients - intersection
