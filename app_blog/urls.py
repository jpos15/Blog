from django.urls import path, include
from .views import HomePageView, post_detalhes

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:post_id>/', post_detalhes, name='detalhes'),
]