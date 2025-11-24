recipes = [
    ("Daiquiri", ["Rum", "Limette", "Zucker"]),
    ("Mojito", ["Rum", "Limette", "Zucker", "Minze", "Soda"]),
    ("Whiskey Sour", ["Whiskey", "Zitrone", "Zucker"]),
    ("Tequila Sour", ["Tequila", "Zitrone", "Zucker"]),
    ("Moscow Mule", ["Vodka", "Limette", "Ginger ale"]),
    ("Munich Mule", ["Gin", "Limette", "Ginger ale"]),
    ("Cuba Libre", ["Rum", "Coke"]),
]


def mixable(
    recipe_list: list[tuple[str, list[str]]], available_ingredients: list[str]
) -> list[str]:
    possible_cocktails = []
    for cocktail, ingredients in recipe_list:
        can_make = True
        for ingredient in ingredients:
            if ingredient not in available_ingredients:
                can_make = False
                break
        if can_make:
            possible_cocktails.append(cocktail)
        # nicer version with list comprehension
        # if all(ingredient in available_ingredients for ingredient in ingredients):
        #     possible_cocktails.append(cocktail)
    return possible_cocktails


assert mixable(recipes, []) == []
assert mixable([], ["Orangensaft"]) == []
assert mixable(recipes, ["Rum", "Whiskey", "Limette", "Zucker", "Coke", "Zitrone"]) == [
    "Daiquiri",
    "Whiskey Sour",
    "Cuba Libre",
]
assert mixable(recipes, ["Rum", "Vodka", "Limette", "Zucker", "Ginger ale"]) == [
    "Daiquiri",
    "Moscow Mule",
]
