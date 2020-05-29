import json
from recipes.models import Recipe

r1 = Recipe(
    title = recipe['recipe_name'],
    description = recipe['description'],
    url = recipe['source_url'],
    dish_image = 'pad_thai.jpeg',
    ingredients = json.dumps(recipe['components']),
    steps = json.dumps(recipe['stages'])
)

r1.save()
