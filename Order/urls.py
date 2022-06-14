from django.urls import re_path
from Order import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^order/$', views.Crud_Order),
    re_path(r'^order/([0-9]+)$', views.Crud_Order),
    re_path(r'^facture/$', views.Crud_Facture),
    re_path(r'^facture/([0-9]+)$', views.Crud_Facture),
    re_path(r'^orderLigne/$', views.Crud_orderLigne),
    re_path(r'^orderLigne/([0-9]+)$', views.Crud_orderLigne),
    re_path(r'^orderByUser/([0-9]+)$', views.get_OrderByUser),
    re_path(r'^orderHistory/([0-9]+)$', views.get_OrderHistory),
    re_path(r'^cart/([0-9]+)$', views.get_Cart),
    re_path(r'^cartItem/([0-9]+)$', views.get_OrderLigne),
    re_path(r'^bestProduct/([0-9]+)$', views.get_Best_product),
    re_path(r'^bestProduct/$', views.get_Best_product),
    re_path(r'^editcartItem/([0-9]+)$', views.edit_OrderLigneQte),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
