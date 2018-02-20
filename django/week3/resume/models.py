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