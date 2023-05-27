from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Certificate(models.Model):
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    discipline = models.CharField(max_length=250, choices=[
        ('Computer Science', 'Computer Science'),
        ('Software Engineering', 'Software Engineering'),
        ('Cyber Security', 'Cyber Security'),
        ('Biochemistry', 'Biochemistry'),
        ('Industrial Chemistry', 'Industrial Chemistry'),
        ('Business Administration', 'Business Administration'),
        ('Mass Communication', 'Mass Communication'),
        ('Criminology', 'Criminology'),
        ('Microbiology', 'Microbiology'),
        ('Economics', 'Economics'),
        ('Accounting', 'Accounting'),
    ])
    institution = models.CharField(max_length=500)
    graduation_date = models.DateField()
    certificate_type = models.CharField(max_length=250, choices=[
        ('Undergraduate', 'Undergraduate'),
        ('Post Graduate', 'Post Graduate'),
    ])
    certificate_no = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images', blank=True)
    qr_code = models.ImageField(upload_to='qrcodes', blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"