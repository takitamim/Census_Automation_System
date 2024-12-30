from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CensusData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='census_entry')

    # Personal Information
    full_name = models.CharField(max_length=100)
    nid_or_birth = models.DecimalField(
    max_digits=20,
    decimal_places=0,
    primary_key=True,
    default= 0  # or any suitable default value
    )
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    marital_status = models.CharField(max_length=20)
    
    # Contact Information
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    # Household Information
    household_members = models.IntegerField()
    household_income = models.DecimalField(max_digits=10, decimal_places=2)
    head_of_household = models.CharField(max_length=50)

    # Employment Information
    employment_status = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    work_sector = models.CharField(max_length=50, blank=True, null=True)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Educational Information
    highest_education = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    currently_enrolled = models.CharField(max_length=50)

    # Housing Information
    house_type = models.CharField(max_length=50)
    house_size = models.IntegerField()
    utilities_available = models.TextField(max_length=255)
    housing_condition = models.CharField(max_length=50)
    living_area = models.CharField(max_length=17)

    def __str__(self):
        return f"{self.email} ({self.user.username})"
    




