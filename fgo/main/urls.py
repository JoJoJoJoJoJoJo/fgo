from django.conf.urls import url
from . import  views


urlpatterns = [
    url(r'^test/$',views.ServantListView.as_view(),name='test_index'),
    url(r'^test/(?P<pk>\d+)/$',views.ServantDetailView.as_view(),name='test_detail'),
]