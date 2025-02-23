# from django.db import models  # Importing Django's models module
# # from django.db
# # Defining the User model
# class User(models.Model):
#     name = models.CharField(max_length=255)  # Character field for storing the name
#     email = models.EmailField(unique=True)   # Email field with unique constraint
#     age = models.IntegerField(default=0)              # Integer field to store age
#     monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal field for salary
#     max_integer = models.BigIntegerField()
    
#     def __str__(self):
#         return self.name  # String representation of the model
 
from  django.db import models
class User(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# user register > login

# task_add -> name , description

# view/

# update
