from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('addmember/',views.add_member),
    path('memberslist/',views.members_list)
]
