from django.test import TestCase, Client
from django.urls import reverse
from census.models import CensusData
from django.contrib.auth.models import User


class CensusViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

        # URL for census page (update if your URL name is different)
        self.url = reverse('censusPage')

        # Create CensusData linked to the test user
        self.entry = CensusData.objects.create(
            user=self.user,
            full_name='John Doe',
            nid_or_birth='1234567890',
            dob='1990-01-01',
            gender='male',  # match form choice
            marital_status='unmarried',  # match form choice
            address='123 Main St',
            city='dhaka',
            division='dhaka',
            zip_code='1200',
            country='bangladesh',
            phone='01712345678',
            email='john@example.com',
            household_members=4,
            household_income=50000,
            head_of_household='yes',
            employment_status='employed',
            occupation='Engineer',
            work_sector='government',
            monthly_income=40000,
            highest_education='bachelor',
            field_of_study='engineering',
            currently_enrolled='no',
            house_type='apartment',
            house_size=1200,
            utilities_available='electricity,water',  # likely stored as string in DB
            housing_condition='good',
            living_area='urban',
        )

    def test_census_page_view_post_valid(self):
    # Remove existing CensusData for this user before posting
        CensusData.objects.filter(user=self.user).delete()

        post_data = {
            'full_name': 'Jane Smith',
            'nid_or_birth': '0987654321',
            'dob': '1995-05-05',
            'gender': 'male',  # match your form choices (lowercase probably)
            'marital_status': 'unmarried',
            'address': '456 New St',
            'city': 'dhaka',
            'division': 'dhaka',
            'zip_code': '1212',
            'country': 'bangladesh',
            'phone': '01812345678',
            'email': 'jane@example.com',
            'household_members': 3,
            'household_income': 60000,
            'head_of_household': 'yes',
            'employment_status': 'employed',
            'occupation': 'Doctor',
            'work_sector': 'private',
            'monthly_income': 45000,
            'highest_education': 'master',
            'field_of_study': 'medicine',
            'currently_enrolled': 'no',
            'house_type': 'concrete',
            'house_size': 1300,
            'utilities_available': ['electricity', 'water'],  # if your form handles this as a multiple choice
            'housing_condition': 'good',
            'living_area': 'urban',
            # 'user': self.user.id,  # Usually user is linked from request.user in view, so not needed here
        }

        response = self.client.post(self.url, post_data)
        self.assertEqual(response.status_code, 302)



    def test_census_page_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Full Name')  # Check form label or something in page

    def test_update_form_view(self):
        url = reverse('update_form', args=[self.entry.nid_or_birth])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_update_form_view_invalid_id(self):
        url = reverse('update_form', args=[999999])  # Large ID unlikely to exist
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


