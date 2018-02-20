from django.shortcuts import render
from .models import Experience, Education, Resume

# Create your views here.
def home(request):
    '''
    Renders the Resume app home template.
    Returns resume/home.html
    '''
    user_resume = Resume.objects.first()
    context = {'resume':user_resume}
    return render(request, 'resume/home.html', context)