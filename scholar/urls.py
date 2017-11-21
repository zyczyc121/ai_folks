from django.conf.urls import url

from . import views
import scholar.views

app_name = 'scholar'
urlpatterns = [
    url(r'^$', scholar.views.field_rank, name='field_rank'),
    url(r'^field/(?P<field>.+)$', scholar.views.field_rank, name='field_rank'),
    url(r'^profile/(?P<scholar_pk>\d+)$', scholar.views.profile, name='profile'),
]
