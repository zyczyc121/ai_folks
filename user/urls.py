from django.conf.urls import url
import user.views

app_name = 'user'

urlpatterns = [
    url(r'^login/$', user.views.login, name='login'),
    url(r'^logout/$', user.views.logout, name='logout'),
    url(r'^signup/$', user.views.signup, name='signup'),
]
