
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('indexhome/',views.indexhome,name='aindexhome'),
    path('staffhome/',views.staffhome,name='staffhome'),
    path('studenthome/',views.studenthome,name='studenthome'),

    path('register/', views.registration_form, name='registration_form'),

]