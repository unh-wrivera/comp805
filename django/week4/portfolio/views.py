from django.shortcuts import render
from resume.models import Experience, Education 
def home(request):
    """
    Renders home page.
    """
    context ={ }
    return render(request, 'home.html', context = None)
 
def resume(request):
    """
    Renders resume page.
    """
    qs1 = Experience.objects.all()
    qs2 = Education.objects.all()
    context = {'experience': qs1, 'education':qs2}
    return render(request, 'resume/home.html', context)

def portfolio(request):
    """
    Renders portfolio page.
    """
    context ={ }
    return render(request, 'portfolio.html', context = None)

def contact(request):
    """
    Renders contact page.
    """
    context ={ }
    return render(request, 'contact.html', context = None)