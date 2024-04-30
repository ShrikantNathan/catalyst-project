from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UploadedData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CompanyDataModel(models.Model):
    # domain,year founded,	industry, size range, locality,	country, linkedin url, current employee estimate, total employee estimate
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=100)
    size_range = models.IntegerField()
    locality = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    linkedin_url = models.CharField(max_length=200)
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()

    def __str__(self) -> str:
        return self.name.title()

class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

class UserQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    employees_from = models.IntegerField()
    employees_to = models.IntegerField()