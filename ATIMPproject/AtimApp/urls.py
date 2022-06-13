from django.urls import path
from . import views

urlpatterns = [
    path('add_university', views.add_university, name='add_university'),
    path('display_university', views.display_university, name="display_university"),
    path('update_university/<int:university_id>', views.update_university, name='update_university'),
    path('delete_university/<int:university_id>', views.delete_university, name='delete_university'),
    path('graduate_student_info_by_university', views.graduate_student_info_by_university,
         name='graduate_student_info_by_university'),
    path('graduate_status_by_university/<student_id>', views.graduate_status_by_university,
         name='graduate_status_by_university'),

    path('add_company', views.add_company, name='add_company'),
    path('display_company', views.display_company, name="display_company"),
    path('update_company/<int:company_id>', views.update_company, name='update_company'),
    path('delete_company/<int:company_id>', views.delete_company, name='delete_company'),
    path('display_all_graduate_student', views.display_all_graduate_student, name='display_all_graduate_student'),
    path('add_job_offer', views.add_job_offer, name='add_job_offer'),

    path('add_graduate_student', views.add_graduate_student, name='add_graduate_student'),
    path('display_graduate_student', views.display_graduate_student, name='display_graduate_student'),
    path('Search_by_major/<major>', views.Search_by_major, name='Search_by_major'),
    path('update_graduate_student/<int:student_id>', views.update_graduate_student, name='update_graduate_student'),
    path('delete_graduate_student/<int:student_id>', views.delete_graduate_student, name='delete_graduate_student'),

    path('display_graduate_student_status', views.display_graduate_student_status,
         name='display_graduate_student_status'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('update_student_profile/<int:offer_id>', views.update_student_profile, name='update_student_profile'),

]
