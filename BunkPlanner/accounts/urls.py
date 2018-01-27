from django.conf.urls import url
from . import views



app_name='accounts'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.login,name='login'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),

]
