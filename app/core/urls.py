from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('marks/add/', views.marks_create, name='marks_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/',views.student_update, name='student_update'),
    path('students/<int:pk>/delete/',views.student_delete, name='student_delete'),
    path('students/<int:pk>/report/', views.student_report, name='student_report'),
    path(
    'students/<int:pk>/export/details/',views.export_student_details_csv,name='export_student_details'),
    path('students/<int:pk>/export/marks/', views.export_student_marks_csv,name='export_student_marks'),
    path('export/students/excel/',views.export_all_students_excel,name='export_all_students_excel'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("attendance/mark/", views.mark_attendance, name="mark_attendance"),
    path("attendance/view/", views.view_attendance, name="view_attendance"),
    path("my/", views.student_dashboard, name="student_dashboard"),
    path("my/attendance/", views.student_attendance, name="student_attendance"),
    path("my/attendance/monthly/", views.student_monthly_attendance, name="student_monthly_attendance"),









    
]