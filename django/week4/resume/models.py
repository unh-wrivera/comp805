from django.db import models

# Create your models here.
class Resume(models.Model):
    #Resume table fields
    first_name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)

    def get_full_name(self):
        """
        Params: self
        Returns a user's entire name; first name first,  last name last
        """
        return "Name (First, Last): {} {}".format(self.first_name, self.last_name)

    def get_last_name_first_name(self):
        """
        Params: self
        Returns a user's entire name; last name first,  first name last
        """
        return "Name (Last, First): {} {}".format(self.last_name, self.first_name)
    def get_experience(self):
        """
        Params: self
        Returns a user's set of experiences to build a resume
        """
        return self.experience_set.all()

    def get_education(self):
        """
        Params: self
        Returns a user's set of education information to build a resume
        """
        return self.education_set.all()


class Experience(models.Model):
    #FK to Resume Table
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)
    #Experience table fields
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()

 #   def __str__(self):
 #       return self.title


class Education(models.Model):
    #FK to Resume Table
    resume= models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)
    #Education table fields
    institution_name = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=True)
    degree = models.CharField(max_length=255, null=False, blank=True)
    major = models.CharField(max_length=255, null=False, blank=True)
    gpa = models.FloatField(null=False, blank=True)

#    def __str__(self):
#        return self.institution_name

