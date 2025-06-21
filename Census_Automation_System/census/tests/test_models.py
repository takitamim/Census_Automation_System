# census/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from census.models import CensusData
from django.core.exceptions import ValidationError

class CensusDataModelTest(TestCase):

    def test_invalid_email(self):
        user = User.objects.create_user(username='u2', password='pass')
        census = CensusData(
            user=user,
            full_name="Invalid Email",
            nid_or_birth=123,
            gender="male",
            dob="2001-01-01",
            marital_status="unmarried",
            address="Test",
            city="Dhaka",
            division="dhaka",
            zip_code="1200",
            country="Bangladesh",
            phone="01234567890",
            email="not-an-email",  # Invalid
            household_members=3,
            household_income=10000.00,
            head_of_household="yes",
            employment_status="unemployed",
            occupation="None",
            work_sector="none",
            monthly_income=0.0,
            highest_education="None",
            field_of_study="None",
            currently_enrolled="no",
            house_type="hut",
            house_size=300,
            utilities_available="none",
            housing_condition="poor",
            living_area="rural"
        )

        with self.assertRaises(ValidationError):
            census.full_clean()  # 🔑 Triggers validation
