from colorama import Fore, Style


class Recipe:
    
    def __init__(self, id, name, category, instructions, ingredients, measures):
        self.id = id
        self.name = name
        self.category = category
        self.instructions = instructions
        self.ingredients = ingredients
        self.measures = measures

    def __str__(self):
        s = "*" * 30
        im = ""
        for ingredient, measure in zip(self.ingredients, self.measures):
            im += f"\n{ingredient}: {measure}"

        return Fore.MAGENTA + Style.BRIGHT + f"""
{s}
Recipe: {self.name}

Category: {self.category}

Ingredients: {im}

Instructions: {self.instructions}
{s}
"""
