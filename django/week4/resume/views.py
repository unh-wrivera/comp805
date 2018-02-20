from django.shortcuts import render
from .models import Resume, Experience, Education

# Create your views here.
def home(request):
    '''
    Params: request
    Renders the Resume app home template.
    Returns resume/home.html
    '''
    resume = Resume.objects.first()
    context = {'resume':resume}
    return render(request, 'resume/home.html', context)