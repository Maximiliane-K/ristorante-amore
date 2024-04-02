from django.db import models

# Create your models here.
class About(models.Model):
    """
    Model for About section on landing page
    """
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title

class Category(models.Model):
    """
    Model for menu items categories 
    """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class MenuItems(models.Model):
    """
    Model for the menu items
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category,related_name='menu_items', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return self.name