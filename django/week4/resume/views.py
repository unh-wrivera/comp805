from django.shortcuts import render
from .models import Experience, Education

# Create your views here.
def home(request):
    '''
    Renders the Resume app home template.
    '''
    qs1 = Experience.objects.all()
    qs2 = Education.objects.all()
    context = {'experience': qs1, 'education':qs2}
    return render(request, 'resume/home.html', context)