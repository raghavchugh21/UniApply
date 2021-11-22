from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

User = get_user_model()

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class Campus(models.Model):
    name = models.CharField(max_length=50)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Job(models.Model):
    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = RichTextField()
    prerequisites = TaggableManager(blank=True)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    campus = models.ForeignKey(Campus, related_name='Campus', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    org_name = models.CharField(max_length=300)
    last_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Function to return a list of prerequisite course names
    def get_prereqs(self):
        return list(self.prerequisites.names())


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.job.title


class BookmarkJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.job.title
