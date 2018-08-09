from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.graphs, name='graphs'),
    re_path('get_data/(?P<graph_type>.+)/$', views.get_data, name='get_data'),
]
