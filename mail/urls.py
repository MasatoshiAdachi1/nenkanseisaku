from django.urls import path
from . import views

app_name = "mail"

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contactFn/', views.contactFn, name='contactFn'),
    path('thanks/', views.thanks, name='thanks'),
]