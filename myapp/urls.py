from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin 
from myapp import admin
from . import views
from django.conf.urls.static import static


urlpatterns = [
    # General pages
    path('', views.index, name='index'),
    path('login/', views.LoginPage, name='loginPage'), 
    path('loginpg/', views.login_auth, name='auth'),  # Login authentication
    path('mainpg/', views.main, name='mainpage'), 
    path('aboutpg/', views.about, name='aboutus'), 
    path('exampg/', views.exam, name='exampg'),
    path('signuppg/', views.signupPage, name='signuppage'),
    path('signup/', views.signup, name='signup'), 
    path('show/', views.show, name='show'),
    path('home/', views.home, name='home'),
    path('edit/<int:id>/', views.edit, name='edit'),  
    path('update/<int:id>/', views.update, name='update'), 
    path('delete/<int:id>/', views.destroy, name='delete'), 
    path('search/', views.search_users, name='search_users'),
    path('upload/', views.upload_file, name='upload'),
    path('download/', views.download_file, name='download'),
    path('generate_excel_report_task/', views.generate_excel_report_task, name='generate_excel_report_task'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('job-list/', views.jobListing, name='job-list'),
    path('logout/', views.user_logout, name='logout'),


    # Custom login and logout views
    path('admin/logout/', views.CustomAdminLogoutView.as_view(), name='admin_logout'),

    # Admin panel login (using Django's default admin login view)
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='admin_login'),
    #path('admin/', admin.site.urls),  # Admin URLs

    # Jobs
     path('apply/', views.apply_job, name='apply_job'),
    #View application
    path('applications/', views.view_applications, name='view_applications'),
    #Specific
    path('jobapplications/', views.job_applications_view, name='job_applications'),
     path('admin/job_applications/excel/', views.excel_job_applicants, name='excel_job_applicants'),  # Excel export 
    #DIrect
    path('applyjob/<int:job_id>/', views.applyjob, name='applyjob'),
    path('jobs/post/', views.post_job, name='post_job'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    #Manage Jobs Urls
    path('admin/job_listings/excel/', views.excel_job_list, name='excel_job_list'),  # URL for JobExcel export
    path('jobs/edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('jobs/delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('test/excel/', views.test_excel_export, name='test_excel_export'),
    path('test/excel/job', views.test_excel_job, name='test_excel_job'),
    path('send-email/<int:applicant_id>/', views.send_email, name='send_email'),   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

