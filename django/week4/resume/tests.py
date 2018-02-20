from django.test import TestCase
from .models import Resume, Education, Experience

# Create your tests here.
class ResumeTestCase(TestCase):
    resume = None
    experience = None 
    education = None

    def setUp(self):
        '''
        Sets up our testing fixture and 
        creates objects which we can use in future tests.
        '''
        self.resume = Resume.objects.create(
                                            first_name='John',
                                            last_name='Doe',
            )

        self.experience = Experience.objects.create(
                                            title='Astrobiologist',
                                            location='NASA',
                                            start_date ='2000-01-01',
                                            end_date ='2010-10-10',
                                            description='Learn all of the'+
                                             ' science about living things'+
                                             ' in space.',

            )

        self.education= Education.objects.create(
                                            institution_name='Hard Knocks University',
                                            location='Manch Vegas, USA',
                                            degree= 'BS',
                                            major= 'Ebonics',
                                            gpa=1.23,
            )

    def test_get_full_name(self):
        '''
        Tests the get_full_name() function.
        Params: self
        Returns: Nothing
        '''
        someguy = 'John Doe'
        self.assertEqual(someguy, self.resume.get_full_name())

    def test_get_last_name_first_name(self):
        '''
        Tests the get_last_() function.
        Params: self
        Returns: Nothing
        '''
        backwards_name = 'Doe John'
        self.assertEqual(backwards_name, self.resume.get_last_name_first_name())

    def test_get_experience(self):
        '''
        Tests the get_experience() function.
        Params: self
        Returns: Nothing
        '''
        self.assertEqual(list(self.resume.get_experience()), 
            list(self.resume.experience_set.all()))


    def test_get_education(self):
        '''
        Tests the get_full_name() function.
        Params: self
        Returns: Nothing
        '''
        self.assertEqual(list(self.resume.get_education()), 
            list(self.resume.education_set.all()))
