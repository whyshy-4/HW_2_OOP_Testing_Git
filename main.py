# Ваш код здесь
class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f'{self.name}: {self.quantity} {self.unit}'

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        quantity = float(quantity)
        if quantity <= 0: raise ValueError("Количество должно быть положительным")
        self._quantity = quantity

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit


# Ваш код здесь
class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = []
        if ingredients is not None:
            for i in ingredients: self.add_ingredient(i)

    def add_ingredient(self, ingredient):
        for j in self.ingredients:
            if j == ingredient:
                j.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return  ratio > 0

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        return f'Для блюда {self.title} необходимы ингредиенты: {self.ingredients}'

    def scale(self, ratio):
        ingredients_new = []
        for k in self.ingredients:
            ingredient_new = Ingredient(k.name, k.quantity*ratio, k.unit)
            ingredients_new.append(ingredient_new)
        return Recipe(self.title, ingredients_new)

# Ваш код здесь
class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0: raise ValueError("Количество порций должно быть положительным")
        recipe__scaled = recipe.scale(portions)
        for ingredient in recipe__scaled.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title):
        for i in range(len(self._items) - 1, -1, -1):
            if self._items[i][1] == title:
                self._items.pop(i)

    def get_list(self):
        dictt = {}
        for i in self._items:
            ingredient = i[0]
            key = (ingredient.name, ingredient.unit)
            if key in dictt: dictt[key] += ingredient.quantity
            else: dictt[key] = ingredient.quantity
        result = []
        for key, quantity in dictt.items():
            name, unit = key[0], key[1]
            result.append(Ingredient(name, quantity, unit))
        result.sort(key=lambda x: x.name)
        return result

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items +other._items
        return new_list

# Ваш код здесь
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio):
        new_scaled = super().scale(ratio)
        return DietaryRecipe(self.title, self.diet_type, new_scaled.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"

