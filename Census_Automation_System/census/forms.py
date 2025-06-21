from django import forms
from .models import CensusData

class CensusForm(forms.ModelForm):
    utilities_available = forms.MultipleChoiceField(
        label="Utilities Available",
        choices=[
            ('electricity', 'Electricity'),
            ('water', 'Water'),
            ('gas', 'Gas'),
            ('internet', 'Internet'),
            ('other', 'Other'),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        required=False)

    

    class Meta:
        model = CensusData
        fields = '__all__'  # Include all fields from the model
        exclude = ['user']  # Exclude the user field to prevent modification
        labels = {
            # Personal Information
            'full_name': 'Full Name',
            'nid_or_birth': 'NID or Birth Certificate Number',
            'gender': 'Gender',
            'dob': 'Date of Birth',
            'marital_status': 'Marital Status',
            
            # Contact Information
            'address': 'Address',
            'city': 'District',
            'division': 'Division',
            'zip_code': 'Zip/Postal Code',
            'country': 'Country',
            'phone': 'Phone Number',
            'email': 'Email Address',
            
            # Household Information
            'household_members': 'Number of Household Members',
            'household_income': 'Total Monthly Household Income (BDT)',
            'head_of_household': 'Is the Respondent Head of Household?',
            
            # Employment Information
            'employment_status': 'Employment Status',
            'occupation': 'Occupation (if applicable)',
            'work_sector': 'Sector of Employment',
            'monthly_income': 'Monthly Income (BDT)',
            
            # Educational Information
            'highest_education': 'Highest Level of Education Attained',
            'field_of_study': 'Field of Study (if applicable)',
            'currently_enrolled': 'Currently Enrolled in Education?',
            
            # Housing Information
            'house_type': 'Type of House',
            'house_size': 'House Size (in square feet)',
            'utilities_available': 'Utilities Available',
            'housing_condition': 'Condition of the House',
            'living_area' : 'In which area you are currently living in?',
        }
        # Widgets for enhanced form usability
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            'gender': forms.Select(choices=[
                ('male', 'Male'),
                ('female', 'Female'),
                ('other', 'Other')
            ], attrs={'class': 'form-control'}),

            'marital_status': forms.Select(choices=[
                ('married', 'Married'),
                ('unmarried', 'Unmarried')
            ], attrs={'class': 'form-control'}),

            'division': forms.Select(choices=[
                ('dhaka', 'Dhaka'),
                ('chittagong', 'Chittagong'),
                ('rajshahi', 'Rajshahi'),
                ('khulna', 'Khulna'),
                ('barishal', 'Barishal'),
                ('rangpur', 'Rangpur'),
                ('sylhet', 'Sylhet'),
                ('mymensingh', 'Mymensingh')
            ], attrs={'class': 'form-control'}),


            'work_sector': forms.Select(choices=[
                ('government', 'Government'),
                ('private', 'Private'),
                ('ngo', 'NGO'),
                ('freelance', 'Freelance'),
                ('other', 'Other')
            ], attrs={'class' : 'form-control'}),

            'field_of_study': forms.Select(choices=[
                ('none', 'None'),
                ('science', 'Science'),
                ('arts', 'Arts'),
                ('commerce', 'Commerce'),
                ('engineering', 'Engineering'),
                ('medicine', 'Medicine'),
                ('other', 'Other')
            ], attrs={'class': 'form-control'}),

            'housing_condition': forms.Select(choices=[
                ('excellent', 'Excellent'),
                ('fair', 'Fair'),
                ('good', 'Good'),
                ('poor', 'Poor')
            ], attrs={'class': 'form-control'}),

            'currently_enrolled' : forms.Select(choices=[
                ('yes', 'Yes'), 
                ('no', 'No')
                ], attrs={'class': 'form-control'}),

            'head_of_household' : forms.Select(choices=[
                ('yes', 'Yes'), 
                ('no', 'No')
                ], attrs={'class': 'form-control'}),

            'living_area' : forms.Select(choices=[
                ('urban', 'Urban'), 
                ('rural', 'Rural')
                ], attrs={'class': 'form-control'}),


            'country': forms.Select(choices=[
                ('bangladesh', 'Bangladesh'),
                ('abroad', 'Abroad')
            ], attrs = {'class': 'form-control'}),

            'employment_status': forms.Select(choices=[
                ('employed', 'Employed'),
                ('unemployed', 'Unemployed'),
                ('student', 'Student'),
                ('retired', 'Retired'),
                ('other', 'Other')
            ], attrs={'class': 'form-control'}),


            'house_type': forms.Select(choices=[
                ('apartment', 'Apartment'),
                ('bungalow', 'Bungalow'),
                ('townhouse', 'Townhouse'),
                ('other', 'Other')
            ], attrs={'class': 'form-control'}),

            'utilities_available': forms.TextInput(attrs={'placeholder': 'e.g., Electricity, Water, Internet', 'class': 'form-control'}),

            'household_income': forms.NumberInput(attrs={'class': 'form-control'}),

            'monthly_income': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_house_size(self):
        house_size = self.cleaned_data.get('house_size')
        if house_size is not None and house_size <= 0:
            raise forms.ValidationError("House size must be a positive number.")
        return house_size

