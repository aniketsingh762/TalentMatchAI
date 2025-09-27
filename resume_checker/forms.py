from django import forms
from django.forms import widgets

from resume_checker.models import Resume


class ResumeForm(forms.ModelForm):
    # Add filtering fields
    experience_level = forms.ChoiceField(
        choices=[
            ('', 'All Levels'),
            ('entry', 'Entry Level (0-2 years)'),
            ('mid', 'Mid Level (3-5 years)'),
            ('senior', 'Senior Level (6+ years)')
        ],
        required=False,
        widget=forms.Select(attrs={
            'class': 'custom-select w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white'
        })
    )
    
    skills_focus = forms.ChoiceField(
        choices=[
            ('', 'All Skills'),
            ('technical', 'Technical Skills'),
            ('soft', 'Soft Skills'),
            ('leadership', 'Leadership Skills')
        ],
        required=False,
        widget=forms.Select(attrs={
            'class': 'custom-select w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white'
        })
    )

    class Meta:
        model = Resume
        fields = ["job_title", "resume"]
        labels = {"job_title": "Job Title", "resume": "Resume"}
        widgets = {
            "job_title": widgets.Select(
                attrs={
                    "class": "custom-select w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                }
            ),
            "resume": widgets.FileInput(
                attrs={
                    "class": "hidden",
                    "accept": ".pdf,.txt",
                }
            ),
        }