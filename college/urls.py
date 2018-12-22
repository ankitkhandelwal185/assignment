from django.conf.urls import url, include
from . import views

app_name = 'college'
urlpatterns = [
    url(r'^api/add/college$', views.CollegeDetail.as_view()),
    url(r'^api/get/college/(?P<college_id>[0-9]+)$', views.CollegeDetail.as_view()),
    url(r'^api/add/course$', views.CourseDetail.as_view()),
    url(r'^api/all/course$', views.AllCourses.as_view()),
]
