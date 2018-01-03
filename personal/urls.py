from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^bpolitik/$',views.bpolitik, name='bpolitik'),
    url(r'^bsosi/$',views.bsosi, name='bsosi'),
    url(r'^btekno/$',views.btekno, name='btekno'),
    url(r'^bentertain/$',views.bentertain, name='bentertain'),
    url(r'^bsains/$',views.bsains, name='bsains'),
    url(r'^bekonomi/$',views.bekonomi, name='bekonomi'),
    url(r'^login/$',views.login, name='login'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^berita/$',views.berita, name='berita'),
]
