from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()

 #   def __str__(self):
 #       return self.title


class Education(models.Model):
    institution_name = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=True)
    degree = models.CharField(max_length=255, null=False, blank=True)
    major = models.CharField(max_length=255, null=False, blank=True)
    gpa = models.FloatField(null=False, blank=True)

#    def __str__(self):
#        return self.institution_name

class Resume(models.Model):
    resExperience = models.ForeignKey(Experience, on_delete=models.CASCADE, default=1)
    resEducation= models.ForeignKey(Education, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)

    def get_full_name():
        full_name = first_name + ' ' + last_name
        return full_name
    def get_last_name_first_name():
        reverse_name = last_name + ' ' + first_name
        return reverse_name

    def get_experience():
        return resExperience

    def get_education():
        return resEducation