from django.test import TestCase
from census.forms import CensusForm

class CensusFormTest(TestCase):
    def get_valid_data(self):
        return {
            'full_name': 'John Doe',
            'nid_or_birth': '1234567890',
            'dob': '1990-01-01',
            'gender': 'M',
            'marital_status': 'Single',
            'address': '123 Main St',
            'city': 'Dhaka',
            'division': 'Dhaka',
            'zip_code': '1200',
            'country': 'Bangladesh',
            'phone': '01712345678',
            'email': 'john@example.com',
            'household_members': 4,
            'household_income': 50000,
            'head_of_household': 'Yes',
            'employment_status': 'Employed',
            'highest_education': 'Bachelor',
            'currently_enrolled': 'No',
            'house_type': 'Concrete',
            'house_size': 1200,
            'housing_condition': 'Good',
            'living_area': 'Urban',
        }

    def test_valid_form(self):
        form = CensusForm(data=self.get_valid_data())
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_missing_name(self):
        data = self.get_valid_data()
        data.pop('full_name')
        form = CensusForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)

    def test_missing_age(self):
        data = self.get_valid_data()
        data.pop('dob')
        form = CensusForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('dob', form.errors)

    def test_missing_occupation(self):
        data = self.get_valid_data()
        data.pop('employment_status')
        form = CensusForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('employment_status', form.errors)

    def test_invalid_non_integer_household_members(self):
        data = self.get_valid_data()
        data['household_members'] = 'four'
        form = CensusForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('household_members', form.errors)

    def test_invalid_negative_house_size(self):
        data = self.get_valid_data()
        data['house_size'] = -500
        form = CensusForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('house_size', form.errors)
