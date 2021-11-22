from django.urls import path
from Portal import views

app_name = "Portal"


urlpatterns = [

    # Home Page URL
    path('', views.home_view, name='home'),

    # List of All Jobs URL
    path('jobs/', views.all_jobs_view, name='job-list'),

    # Create Job URL
    path('job/create/', views.create_job_view, name='create-job'),

    # Single Job with job id = id URL
    path('job/<int:id>/', views.single_job_view, name='single-job'),

    # Apply to Job with job id = id URL
    path('apply-job/<int:id>/', views.apply_job_view, name='apply-job'),

    # Bookmark Job with job id = id URL
    path('bookmark-job/<int:id>/', views.bookmark_job_view, name='bookmark-job'),

    # Search Query result URL
    path('result/', views.search_result_view, name='search_result'),

    # User Dashboard URL
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # See All Applications URL
    path('dashboard/teacher/job/<int:id>/applicants/', views.all_applicants_view, name='applicants'),

    # Edit Job URL
    path('dashboard/teacher/job/edit/<int:id>', views.job_edit_view, name='edit-job'),

    # View Applicant URL
    path('dashboard/teacher/applicant/<int:id>/', views.applicant_details_view, name='applicant-details'),

    # Close Job URL
    path('dashboard/teacher/close/<int:id>/', views.make_complete_job_view, name='complete'),

    # Delete Job URL
    path('dashboard/teacher/delete/<int:id>/', views.delete_job_view, name='delete'),

    # Delete Bookmark URL
    path('dashboard/student/delete-bookmark/<int:id>/', views.delete_bookmark_view, name='delete-bookmark'),

]
