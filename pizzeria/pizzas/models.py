from django.db import models

# Create your models here.

class Pizza(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name

class Topping(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name

class Pizza_Topping(models.Model):
  pizza = models.ForeignKey(Pizza)
  name = models.ManyToManyField(Topping)

  def __str__(self):
    return 'toppings for ' + self.pizza.name + ' pizza'
