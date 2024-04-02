from django.shortcuts import render
from .models import About

# Create your views here.
def about_view(request):
    """
    View to display about content on landing page
    """
    about_content = About.objects.all().first()

    context = {'about_content': about_content}

    return render(request, 'index.html', context)