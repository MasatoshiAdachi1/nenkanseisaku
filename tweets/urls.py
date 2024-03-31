from django.urls import path
from . import views

app_name = 'tweets'  # これを追加した

urlpatterns = [
    path("kanri/", views.kanri, name="kanri"),
    path('kanri/post', views.post, name='post'),
    path('view',views.item, name="item")
]