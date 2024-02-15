from django.db import models

# Create your models here.


class Customer(models.Model):
    """
    The `customer` class is a model in Django that represents a customer with attributes such as name,
    email, and phone number.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    # age = models.IntegerField()

    def __str__(self):
        """
        The above function returns a string representation of an object, including its name and email.
        :return: The `__str__` method is returning a string representation of an object. It is returning
        a formatted string that includes the object's name and email attributes.
        """
        return "{} - {}".format(self.name, self.email)

    class Meta:
        """
        The above class defines metadata for a "Customer" model in Python.
        """
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['-id']
