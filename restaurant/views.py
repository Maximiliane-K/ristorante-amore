from django.shortcuts import render
from .models import About, Category, MenuItems

# Create your views here.
def about_view(request):
    """
    View to display about content on landing page
    """
    about_content = About.objects.all().first()

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