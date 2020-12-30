from django import forms
from .models import (
    PublicProcurement,
    Vacancy,

    )

class PublicProcurementCreateForm(forms.ModelForm):
    class Meta:
        model = PublicProcurement
        fields = ['publicprocurement_title', 'publicprocurement_image',
                  'published_status', 'website_link'
        ]

class VacancyCreateForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['vacancy_title', 'vacancy_image',
                  'vacancy_published_status', 'vacancy_website_link'
        ]