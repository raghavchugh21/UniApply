from django.urls import path
from Account import views

app_name = "Account"

urlpatterns = [

    # Student Registration URL
    path('student/register/', views.student_registration, name='student-registration'),

    # Teacher Registration URL
    path('teacher/register/', views.teacher_registration, name='teacher-registration'),

    # Edit Student Profile URL
    path('profile/edit/<int:id>/', views.student_edit_profile, name='edit-profile'),

    # Login URL
    path('login/', views.user_logIn, name='login'),

    # Logout URL
    path('logout/', views.user_logOut, name='logout'),

]
