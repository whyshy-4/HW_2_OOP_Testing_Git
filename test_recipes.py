import pytest
from main import Ingredient, Recipe, DietaryRecipe, ShoppingList

def test_init():
    i = Ingredient("Мука", 500.0, "г")
    assert i.name == "Мука"
    assert i.quantity == 500.0
    assert i.unit == "г"

def test_str():
    i = Ingredient("Мука", 500.0, "г")
    assert str(i) == "Мука: 500.0 г"

def test_eq():
    assert Ingredient("Мука", 500.0, "г") == Ingredient("Мука", 300.0, "г")
    assert Ingredient("Мука", 500.0, "г") != Ingredient("Сахар", 500.0, "г")
    assert Ingredient("Мука", 500.0, "г") != Ingredient("Мука", 500.0, "кг")

def test_init1():
    i = Recipe("Пицца", [Ingredient("Мука", 500.0, "г")])
    assert i.title == "Пицца"
    assert len(i.ingredients) == 1

def test_add():
    i = Recipe("Пицца", [])
    i.add_ingredient(Ingredient("Мука", 500.0, "г"))
    i.add_ingredient(Ingredient("Мука", 300.0, "г"))
    assert len(i.ingredients) ==1
    assert i.ingredients[0].quantity == 800.0

def test_scale():
    i = Recipe("Пицца", [Ingredient("Мука", 500.0, "г")])
    i_new = i.scale(2.0)
    assert i_new.ingredients[0].quantity==1000.0
    with pytest.raises(ValueError):
        i.scale(-1)

def test_len():
    i = Recipe("Пицца", [Ingredient("Мука", 500.0, "г")])
    assert len(i) == 1

def test_add_recipe():
    i = ShoppingList()
    i.add_recipe(Recipe("Пицца", [Ingredient("Мука", 500.0, "г")]), 2.0)
    assert len(i._items) == 1
    with pytest.raises(ValueError): i.add_recipe(Recipe("Пицца", []), -1)

def test_remove_recipe():
    i = ShoppingList()
    i.add_recipe(Recipe("Пицца", [Ingredient("Мука", 500.0, "г")]), 1.0)
    i.remove_recipe("Пицца")
    assert len(i._items) == 0
    i.remove_recipe("Торт")

def test_get_list():
    i = ShoppingList()
    i.add_recipe(Recipe("Пицца", [Ingredient("Мука", 500.0, "г")]), 1.0)
    i.add_recipe(Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")]), 1.0)
    lst = i.get_list()
    assert len(lst) == 1
    assert lst[0].quantity == 1000.0

def test_add1():
    i = ShoppingList()
    i.add_recipe(Recipe("Пицца", [Ingredient("Мука", 500.0, "г")]), 1.0)
    i2 = ShoppingList()
    i2.add_recipe(Recipe("Хлеб", [Ingredient("Сахар", 100.0, "г")]), 1.0)
    i3 = i+i2
    assert len(i3._items) == 2