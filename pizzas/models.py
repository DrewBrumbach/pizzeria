from django.db import models

# Structure of the Database is decided here- classes, attributes, etc.
#
# Don't forget that whenever you make an app here, you must include it in the settings
# where you define the other apps
#
# Whenever you make changes to the database, you must make a migration and migrate
#
# Finally, when you make changes here, you must add them to the admin.py file as well.
class Pizza(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        return self.text


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.text[:20]}..."
