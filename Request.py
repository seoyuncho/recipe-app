import requests
from Category import Category
from Meal import Meal
from Recipe import Recipe


# API base URL
BASE_URL = "https://www.themealdb.com/api/json/v1/1"
favorite_recipes = {}


def getCategories():
    """
    get all meal categories from themealdb
    """
    url = f"{BASE_URL}/categories.php"
    try:
        r = requests.get(url)
        r.raise_for_status()
        categories = []

        for c in r.json()['categories']:
            category = Category(c['idCategory'], c['strCategory'], c['strCategoryDescription'])
            categories.append(category)
    except requests.exceptions as e:
        print(f"Error fetching categories: {e}")
        return None
    else:
        return categories

def getMealsBy(category):
    """
    get every meal of the selected category
    """
    url = f"{BASE_URL}/filter.php?c={category}"
    try:
        r = requests.get(url)
        r.raise_for_status()
        meals = []

        for m in r.json()['meals']:
            meal = Meal(m['idMeal'], m['strMeal'])
            meals.append(meal)
    except requests.exceptions as e:
        print(f"Error fetching categories: {e}")
        return None
    else:
        return meals


def getMealByName(name):
    """
    get a meal by name and its recipe
    """
    name = name.title().replace(" ", "_")
    url = f"{BASE_URL}/search.php?s={name}"
    try:
        r = requests.get(url)
        r.raise_for_status()
        json = r.json()
        if json and 'meals' in json and json['meals'] is None:
            return None
        m = r.json()['meals'][0]

        i = 1
        ingredients = []
        measures = []
        while m[f'strIngredient{i}'] != '':
            ingredients.append(m[f'strIngredient{i}'])
            measures.append(m[f'strMeasure{i}'])
            i += 1
        instructions = m['strInstructions']
        meal = m['strMeal']
        id = m['idMeal']
        category = m['strCategory']
        recipe = Recipe(id, meal, category, instructions, ingredients, measures)
    except requests.exceptions as e:
        print(f"Error fetching categories: {e}")
        return None
    else:
        return recipe


def getMealByRandom():
    """
    get a random meal and its recipe
    """
    url = f"{BASE_URL}/random.php"
    try:
        r = requests.get(url)
        r.raise_for_status()
        json = r.json()
        if json and 'meals' in json and json['meals'] is None:
            return None
        m = r.json()['meals'][0]

        i = 1
        ingredients = []
        measures = []
        while m.get(f'strIngredient{i}') != '':
            ingredients.append(m[f'strIngredient{i}'])
            measures.append(m[f'strMeasure{i}'])
            i += 1
        instructions = m['strInstructions']
        meal = m['strMeal']
        id = m['idMeal']
        category = m['strCategory']
        recipe = Recipe(id, meal, category, instructions, ingredients, measures)
    except requests.exceptions as e:
        print(f"Error fetching categories: {e}")
        return None
    else:
        return recipe



def getAreas():
    """
    get all areas from themealdb
    """
    url = f"{BASE_URL}/list.php?a=list"
    try:
        r = requests.get(url)
        r.raise_for_status()
        areas = []
        json = r.json()
        if json and 'meals' in json and json['meals'] is None:
            return None
        for a in r.json()['meals']:
            areas.append(a['strArea'])
    except requests.exceptions as e:
        print(f"Error fetching categories: {e}")
        return None
    else:
        return areas


def getMealsByArea(area):
    """
    get every meal of the selected area 
    """
    url = f"{BASE_URL}/filter.php?a={area}"
    
    try:
        r = requests.get(url)
        r.raise_for_status()
        meals = []
        json = r.json()
        if json and 'meals' in json and json['meals'] is None:
            return None
    
        for m in r.json()['meals']:
            meal = Meal(m['idMeal'], m['strMeal'])
            meals.append(meal)      
    except requests.exceptions as e:
        print(f"Error fetching categories: {e}")
        return None
    else:
        return meals


def saveToFavorites(recipe):
    """
    save a recipe to the favorites list
    """
    if recipe.id not in favorite_recipes:
        favorite_recipes[recipe.id] = recipe
        print(f"{recipe.name} has been added to your favorites.")
    else:
        print(f"{recipe.name} is already in your favorites.")


def listFavorites():
    """
    list all saved favorite recipes
    """
    if favorite_recipes:
        print("Your Favorite Recipes: ")
        for recipe in favorite_recipes.values():
            print(recipe)
    else:
        print("You have no favorite recipes yet.")


def opt1():
    s = "-" * 30
    print("{}\nList all Categories\n{}".format(s, s))

    categories = getCategories()
    for category in categories:
        print(category)
    print(s)


def opt2():
    s = "-" * 30
    print("{}\nList all Meals by Category\n{}".format(s, s))

    categories = getCategories()
    category_choice = int(input("Choose a category by number: ")) - 1
    if 0 <= category_choice < len(categories):
        selected_category = categories[category_choice].name
        meals = getMealsBy(selected_category)
        for meal in meals:
            print(meal)
    else:
        print("Invalid Category Choice")
    print(s)


def opt3():
    s = "-" * 30
    print("{}\nSearch Meal by Name\n{}".format(s, s))
    
    name = input("Enter the meal name: ")
    recipe = getMealByName(name)  
    if recipe:
        print(recipe)
        save = input(f"Do you wnat to save {recipe.name} to your favorites? (y/n)").lower()
        if save == 'y':
            saveToFavorites(recipe)
    else:
        print(f"No meals found for name: {name}")
    print(s)


def opt4():
    s = "-" * 30
    print("{}\nRandom Meal\n{}".format(s, s))
    
    recipe = getMealByRandom()
    if recipe:
        print(recipe)
    print(s)


def opt5():
    s = "-" * 30
    print("{}\nList all Areas\n{}".format(s, s))

    areas = getAreas()
    for area in areas:
        print(area)
    print(s)


def opt6():
    s = "-" * 30
    print("{}\nList all Meals by Area\n{}".format(s, s))
    
    area = input("Enter the area: ")
    meals = getMealsByArea(area)
    if meals:
        for meal in meals:
            print(meal)
    else:
        print(f"No meals found for area: {area}")
    print(s)

def opt8():
    s = "-" * 30
    print("{}\nList Favorite Recipes\n{}".format(s, s))
    listFavorites()
    print(s)