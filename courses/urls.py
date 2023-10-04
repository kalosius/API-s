from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('courses/', views.course_list, name='courses'),
    path('courses/<int:id>', views.course_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
