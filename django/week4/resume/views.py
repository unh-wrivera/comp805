from django.shortcuts import render
from .models import Resume, Experience, Education

# Create your views here.
def home(request):
    '''
    Renders the Resume app home template.
    Returns resume/home.html
    '''
    user_full_name = Resume.objects.first().get_full_name()
    user_resume = Resume.objects.first()
    user_exp = user_resume.get_experience()
    user_educ = user_resume.get_education()
    context = {'resume':user_resume}
    return render(request, 'resume/home.html', context)