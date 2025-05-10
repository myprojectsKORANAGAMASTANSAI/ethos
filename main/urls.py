from . import views
from django.urls import path

urlpatterns = [
    path("",views.main),
    path("home/",views.home),
    path("ethos_admin/",views.login_view),
    path("homepage/",views.homepage)
    #path("user_info/",views.user_info,name='user_info'),
   
    
]