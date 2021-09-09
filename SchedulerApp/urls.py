from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('timetableGeneration/', timetable, name='timetable'),

    path('instructorAdd/', instructorAdd, name='instructorAdd'),
    path('instructorEdit/', instructorEdit, name='instructorEdit'),
    path('instructorDelete/<int:pk>/', instructorDelete, name='deleteinstructor'),

    path('roomAdd/', roomAdd, name='roomAdd'),
    path('roomEdit/', roomEdit, name='roomEdit'),
    path('roomDelete/<int:pk>/', roomDelete, name='deleteroom'),

    path('meetingTimeAdd/', meetingTimeAdd, name='meetingTimeAdd'),
    path('meetingTimeEdit/', meetingTimeEdit, name='meetingTimeEdit'),
    path('meetingTimeDelete/<str:pk>/', meetingTimeDelete, name='deletemeetingtime'),

    path('courseAdd/', courseAdd, name='courseAdd'),
    path('courseEdit/', courseEdit, name='courseEdit'),
    path('courseDelete/<str:pk>/', courseDelete, name='deletecourse'),

    path('departmentAdd/', departmentAdd, name='departmentAdd'),
    path('departmentEdit/', departmentEdit, name='departmentEdit'),
    path('departmentDelete/<int:pk>/', departmentDelete, name='deletedepartment'),

    path('sectionAdd/', sectionAdd, name='sectionAdd'),
    path('sectionEdit/', sectionEdit, name='sectionEdit'),
    path('sectionDelete/<str:pk>/', sectionDelete, name='deletesection'),

    path('api/genNum/', apiGenNum, name='apiGenNum'),
    path('api/terminateGens/', apiterminateGens, name='apiterminateGens')
]
