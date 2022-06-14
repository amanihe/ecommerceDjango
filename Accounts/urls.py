from django.urls import re_path
from Accounts import views


from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^user/$', views.Crud_User),
    re_path(r'^supplier/$', views.get_Fnx),
    re_path(r'^user/([0-9]+)$', views.Crud_User),
    re_path(r'^userById/([0-9]+)$', views.get_User),
    re_path(r'^address/$', views.Crud_Address),
    re_path(r'^address/([0-9]+)$', views.Crud_Address),
    re_path(r'^Adrdefault/([0-9]+)$', views.edit_defaultAdress),
    re_path(r'^PersonalAddress/([0-9]+)$', views.get_Address_byUserId),  
    re_path(r'^request/$', views.Crud_Request),
    re_path(r'^request/([0-9]+)$', views.Crud_Request),
    re_path(r'^userRequest/([0-9]+)$', views.get_Request),
     re_path(r'^editrequest/([0-9]+)$', views.edit_Request),
    re_path(r'^login/<str:email>$', views.check_login),
    re_path(r'^userid/<int:id>$', views.get_user),
]
