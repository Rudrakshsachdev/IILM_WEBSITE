from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('login/', views.login_view, name='login'),
    path('profile-completion/', views.profile_completion_view, name='profile_completion'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),
    path('logout/', views.logout_view, name='logout'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('journal-publication/', views.journal_publication_view, name='journal_publication'),
    path('conference-publication/', views.conference_publication_view, name='conference_publication'),
    path('research-projects/', views.research_projects_view, name='research_projects'),
    path('patents/', views.patents_view, name='patents'),
    path('copy-rights/', views.copyrights_view, name='copy_rights'),
    path('phd-guidance/', views.phd_guidance_view, name='phd_guidance'),
    path('book-chapter/', views.book_chapter_view, name='book_chapter'),
    path('book/', views.book_view, name='book'),
    path('consultancy-projects/', views.consultancy_projects_view, name='consultancy_projects'),
    path('editorial-roles/', views.editorial_roles_view, name='editorial_roles'),
    path('reviewer-roles/', views.reviewer_roles_view, name='reviewer_roles'),
    path('awards/', views.awards_view, name='awards'),
    path('industry-collaboration/', views.industry_collaboration_view, name='industry_collaboration'),
    path('form/', views.form_view, name='form_view'),  # 👈 New form view route
    path('submissions/', views.submission_list_view, name='submission_list'),  # 👈 New route for submissions
    # path('submissions/<int:submission_id>/', views.submission_detail_view, name='submission_detail'),  # 👈 Detail view for submissions
    path("update-progress/", views.update_progress, name="update_progress"),
    path("annual-faculty-report/", views.annual_faculty_report_view, name="annual_faculty_report"),
    path("research-grant-application/", views.research_grant_application_view, name="research_grant_application"),
    path("conference-travel-request/", views.conference_travel_request_view, name="conference_travel_request"),
    path("publications-update/", views.publications_update_view, name="publications_update"),
    path("curriculum-development/", views.curriculum_development_view, name="curriculum_development"),
    path("new-submission/", views.new_submission_view, name="new_submission"),
    path("pending-tasks/", views.pending_tasks_view, name="pending_tasks"),
    
    # Review System URLs
    path("review-dashboard/", views.review_dashboard, name="review_dashboard"),
    # path("submission-review/<int:submission_id>/", views.submission_detail_review, name="submission_detail_review"),
    path("my-submissions/", views.my_submissions, name="my_submissions"),
    path("faculty-forms/", views.FacultyForms, name="faculty_forms"),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path("submission/<int:submission_id>/review/", views.review_submission, name="review_submission"),
    path("submission/<int:submission_id>/", views.submission_detail_review, name="submission_detail_review"),


    # Debug route to test static files
    #path('test-static/', views.test_static_view, name='test_static'),
]
