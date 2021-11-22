from django.contrib.auth.models import AbstractUser
from django.db import models
from Account.managers import CustomUserManager
import json
import os
from UniApply.settings import MEDIA_ROOT

JOB_TYPE = (
    ('M', "Male"),
    ('F', "Female"),

)

ROLE = (
    ('student', "Student"),
    ('teacher', "Teacher"),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(choices=ROLE,  max_length=10)
    gender = models.CharField(choices=JOB_TYPE, max_length=1)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_courses(self):
        f = open(os.path.join(MEDIA_ROOT, "json/email_data.json"))
        json_data = json.load(f)
        json_data = json_data["0"]
        courses = []
        for semester in json_data[self.email]['Transcript']:
            if semester != "CGPA":
                for course in json_data[self.email]['Transcript'][semester]:
                    courses.append(course)
        return courses

    def get_cgpa(self):
        f = open(os.path.join(MEDIA_ROOT, "json/email_data.json"))
        json_data = json.load(f)
        return json_data["0"][self.email]["Transcript"]["CGPA"]

    def get_grade(self, course):
        f = open(os.path.join(MEDIA_ROOT, "json/email_data.json"))
        json_data = json.load(f)
        json_data = json_data["0"]
        for semester in json_data[self.email]['Transcript']:
            if semester != "CGPA" and course in json_data[self.email]['Transcript'][semester]:
                return json_data[self.email]['Transcript'][semester][course]
        return "-"

    def get_transcript(self):
        f = open(os.path.join(MEDIA_ROOT, "json/email_data.json"))
        json_data = json.load(f)
        json_data = json_data["0"]
        return json_data[self.email]['Transcript']

    objects = CustomUserManager()
