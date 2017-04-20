from django.conf.urls import include, url
from user_profile import views

urlpatterns = [

    url(r'^$', views.profile, name='profile'),
    url(r'^general_profile_panel/$', views.get_general_profile_panel, name='general_profile_panel'),
    url(r'^general_profile_form/$', views.get_general_profile_form, name='general_profile_form'),
    url(r'^edit_general_profile/$', views.edit_general_profile, name='edit_general_profile'),

]
