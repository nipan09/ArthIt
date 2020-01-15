from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns= [
      url('', LoginView.as_view(template_name= 'registeration/login.html'),name='login'),
      url('app', views.index, name='index'),
      url('sign_up',views.sign_up,name="sign up"),
    ]