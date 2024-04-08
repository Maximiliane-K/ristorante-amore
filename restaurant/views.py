from django.shortcuts import render
from .models import About, Category, MenuItems, BeverageCategory, BeverageItems

# Create your views here.
def about_view(request):
    """
    View to display about content on landing page
    """
    about_content = About.objects.first()

    context = {'about_content': about_content}

    return render(request, 'index.html', context)

def foodmenu(request):
    """
    View to show all food menu items 
    """
    categories = Category.objects.all()
    menu_items = MenuItems.objects.all()
    
    context = {'categories': categories, 'menu_items': menu_items}

    return render(request, 'food.html', context)

def beveragemenu(request):
    """
    View to show all beverages available 
    """
    beverage_categories = BeverageCategory.objects.all()
    beverage_items = BeverageItems.objects.all()
    
    context = {'beverage_categories': beverage_categories, 'beverage_items': beverage_items}

    return render(request, 'drinks.html', context)