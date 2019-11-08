#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    min_quantity = None

    for key in recipe:
        if key not in ingredients:
            return 0
        else: 
            quantity = ingredients[key] // recipe[key]
            if not min_quantity or quantity < min_quantity:
                min_quantity = quantity

    return min_quantity


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))