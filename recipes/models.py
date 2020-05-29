from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.TextField(default="")
    book = models.TextField(default="")
    source = models.CharField(default="", max_length=255)
    dish_image = models.FilePathField(path="/img")
    ingredients = models.TextField()  # A JSON serialized dictionary
    steps = models.TextField()  # JSON serialized cooking steps. Can have form 'super-step 1'/'steps 1...N'
    notes = models.TextField(default="Recipe notes...")  # Flat text fields for notes

