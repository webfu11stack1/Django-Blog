from django.urls import path
from .views import HomePageView, AboutPageview,ContactView

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('about/', AboutPageview.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact')
]