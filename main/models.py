from django.db import models

# Create your models here.
class ToDoList(models.Model):#This line defines a Python class named ToDoList which inherits from models.Model. In Django, each model you define is a Python class that subclasses models.Model.
    name = models.CharField(max_length=200)#This line defines a field named name for the ToDoList model. In this case, it's a CharField, which means it can hold strings of characters. The max_length parameter specifies the maximum length of the string (in this case, 200 characters).
    def __str__(self):#This method defines how instances of the ToDoList model should be represented as strings. In this case, it returns the name attribute of the ToDoList instance, which makes it easier to identify ToDoList objects in the Django admin interface and other contexts.
#To summarize, this code defines a Django model named ToDoList with a single field called name, which represents the name of a to-do list. The __str__ method is overridden to return the name of the to-do list when it's converted to a string. This model can now be used to store and retrieve data related to to-do lists in your Django application's database.
        return  self.name
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)#This line defines a field named todolist for the Item model. It represents a many-to-one relationship with the ToDoList model.

#models.ForeignKey() is a field type in Django used to define many-to-one relationships between models. It's a reference to another model and represents a database foreign key.

#ToDoList is the model to which Item is related. In this case, it's a reference to the ToDoList model.

#on_delete=models.CASCADE specifies the behavior to adopt when the referenced object (in this case, a ToDoList instance) is deleted. CASCADE means that when the referenced ToDoList instance is deleted, all related Item instances will also be deleted. This ensures referential integrity at the database level.
##we have CharField in TodoList 
    text = models.CharField(max_length=300)
    complete= models.BooleanField()# it is boolean field
    def __str__(self):
        return self.text