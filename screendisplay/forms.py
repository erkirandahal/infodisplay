from django import forms
from .models import (
    PublicProcurement,
    Vacancy,
    Official,
    OfficeInfo,
    )

class PublicProcurementCreateForm(forms.ModelForm):
    class Meta:
        model = PublicProcurement
        fields = ['publicprocurement_title', 'publicprocurement_image', 'published_status', 'website_link']

class VacancyCreateForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['vacancy_title', 'vacancy_image', 'vacancy_published_status', 'vacancy_website_link']

class OfficialCreateForm(forms.ModelForm):
    class Meta:
        model = Official
        fields = ['official_name', 'official_designation', 'official_phoneno', 'official_roomno', 'official_published_status', 'official_image']


class OfficeCreateForm(forms.ModelForm):
    class Meta:
        model = OfficeInfo
        fields = ['office_name', 'office_sec_name', 'office_website', 'office_email', 'office_phoneno', 'office_emergencyno', 'office_address_province', 'office_address_district', 'office_address_locallevel', 'office_image']