from django.contrib import admin
from .models import CensusData

@admin.register(CensusData)
class CensusDataAdmin(admin.ModelAdmin):
    # Display all fields in the admin list view
    list_display = (
        'full_name', 'nid_or_birth','gender', 'dob', 'marital_status',
        'address', 'city', 'division', 'zip_code', 'country', 
        'phone', 'email', 'household_members', 'household_income', 
        'head_of_household', 'employment_status', 'occupation', 
        'work_sector', 'monthly_income', 'highest_education', 
        'field_of_study', 'currently_enrolled', 'house_type', 
        'house_size', 'utilities_available', 'housing_condition'
    )
    
    # Add search functionality for relevant fields
    search_fields = (
        'full_name', 'email', 'phone', 'city', 
        'occupation', 'field_of_study'
    )
    
    # Add filters for key fields
    list_filter = (
        'gender', 'marital_status', 'division', 'employment_status', 
        'highest_education', 'house_type', 'currently_enrolled', 
        'head_of_household'
    )
    
    # Optional: Set how many records to show per page
    list_per_page = 25
