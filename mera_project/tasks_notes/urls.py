from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns= [
      url('login', LoginView.as_view(template_name= 'registeration/login.html'),name='login'),
      url('app', views.index, name='index'),
      url(r'^signup/$',views.sign_up,name="sign up"),
      url('add_item', views.add_item, name='add item')
    ]