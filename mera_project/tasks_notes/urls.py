from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

#app_name= 'tasks_notes'

urlpatterns= [
      url(r'^login/$', views.login_view, name='login'),
      url(r'^profile', views.profile_view, name='profile'),
      url(r'^signup/$',views.signup_view,name="sign up"),
      url('add_item', views.additem_view, name='add item'),
    ]