from django import forms
from Portal.models import *
import json
import os
from UniApply.settings import MEDIA_ROOT
from taggit.forms import TagWidget


class JobForm(forms.ModelForm):
    """
        Form for teachers to post a job request on UniApply's Portal
        by taking Job Title, Campus Location, Salary, Job Description,
        Application Deadline and Organisation Name as input. This job
        is listed on the Portal only after moderator's approval.
    """

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Job Title :"
        self.fields['campus'].label = "Campus Location :"
        self.fields['salary'].label = "Salary :"
        self.fields['description'].label = "Job Description :"
        self.fields['prerequisites'].label = "Course Prerequisites :"
        self.fields['last_date'].label = "Application Deadline :"
        self.fields['org_name'].label = "Organisation Name :"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Eg : Research Assistant',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': 'Eg : $800 - $1200/month',
            }
        )
        self.fields['prerequisites'].widget.attrs.update(
            {
                'placeholder': 'Use comma separated values eg: DSA, OS ',
            }
        )
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'Select Date',

            }
        )
        self.fields['org_name'].widget.attrs.update(
            {
                'placeholder': 'Eg: Intermedia Research Group',
            }
        )

    class Meta:
        model = Job

        fields = [
            "title",
            "campus",
            "job_type",
            "salary",
            "description",
            "prerequisites",
            "last_date",
            "org_name",
        ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Service is required")
        return job_type

    def clean_campus(self):
        campus = self.cleaned_data.get('campus')

        if not campus:
            raise forms.ValidationError("Category is required")
        return campus

    # Function to check whether the prerequisites written exist in the
    # university's course list or not. Done using dummy data from
    # course_data.json which represents data retrieved from University's API
    def clean_prerequisites(self):
        prerequisites = self.cleaned_data.get('prerequisites')
        f = open(os.path.join(MEDIA_ROOT, "json/course_data.json"))
        data = json.load(f)
        course_list = data['course_list']
        course_names = [course['course_name'] for course in course_list]
        for prerequisite in prerequisites:
            if prerequisite not in course_names:
                raise forms.ValidationError(prerequisite + " is not a valid course")
        return prerequisites

    def save(self, commit=True):
        job = super(JobForm, self).save(commit=False)
        if commit:
            user.save()
        return job


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['job']


class JobBookmarkForm(forms.ModelForm):
    class Meta:
        model = BookmarkJob
        fields = ['job']


class JobEditForm(forms.ModelForm):
    """
        Form for teachers to edit their job posted on UniApply's Portal
        by taking Job Title, Campus Location, Salary, Job Description,
        Application Deadline and Organisation Name as input.
    """

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Job Title :"
        self.fields['campus'].label = "Campus Location :"
        self.fields['salary'].label = "Salary :"
        self.fields['description'].label = "Job Description :"
        self.fields['prerequisites'].label = "Course Prerequisites :"
        self.fields['last_date'].label = "Application Deadline :"
        self.fields['org_name'].label = "Organisation Name :"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Eg : Research Assistant',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': 'Eg : $800 - $1200/month',
            }
        )
        self.fields['prerequisites'].widget.attrs.update(
            {
                'placeholder': 'Use comma separated values eg: DSA, OS, .. ',
            }
        )
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'Select Date',

            }
        )
        self.fields['org_name'].widget.attrs.update(
            {
                'placeholder': 'Eg: Intermedia Research Group...',
            }
        )

    last_date = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Service Name',
        'class': 'datetimepicker1'
    }))

    class Meta:
        model = Job

        fields = [
            "title",
            "campus",
            "job_type",
            "salary",
            "description",
            "prerequisites",
            "last_date",
            "org_name",
        ]

        widgets = {
            'tags': TagWidget(),
        }

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Service is required")
        return job_type

    def clean_category(self):
        campus = self.cleaned_data.get('campus')

        if not campus:
            raise forms.ValidationError("category is required")
        return campus

    def clean_prerequisites(self):
        prerequisites = self.cleaned_data.get('prerequisites')
        with open(os.path.join(MEDIA_ROOT, "json/course_data.json")) as f:
            data = json.load(f)
            course_list = data['course_list']
            course_names = [course['course_name'] for course in course_list]
            for prerequisite in prerequisites:
                if prerequisite not in course_names:
                    raise forms.ValidationError(prerequisite + " is not a valid course")
        return prerequisites

    def save(self, commit=True):
        job = super(JobEditForm, self).save(commit=False)
        if commit:
            user.save()
        return job
