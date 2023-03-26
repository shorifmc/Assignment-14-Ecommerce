from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog, name= 'home'),
    path('form/',views.show_form, name= 'sform'),
    path('s/',views.student_info, name= 'stdnt'),
    path('successfully/',views.success, name= 'successfully'),

]

