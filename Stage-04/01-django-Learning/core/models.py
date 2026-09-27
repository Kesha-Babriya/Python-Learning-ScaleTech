from django.db import models


# A Django Model is a Python class that represents the structure
# of data we want to store in the database.

# By inheriting from models.Model, Django knows that Student
# should be treated as a database model.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):

    # AutoField automatically generates a unique integer value
    # for each Student record.
    
    # This field acts as the primary key by default.
    id = models.AutoField(primary_key=True)

    # CharField is used to store text/string data.
    name = models.CharField(max_length=100)

    # IntegerField is used to store integer values.
    # default=18 means if we don't provide an age while creating
    age = models.IntegerField(default=18)

    # EmailField is used to store email addresses.
    # Django also provides email-related validation for this field.
    email = models.EmailField()
    course = models.CharField(max_length=100, default="CSE")

    department = models.ForeignKey(Department ,
                                    on_delete= models.CASCADE,
                                    null=True,
                                    blank=True)