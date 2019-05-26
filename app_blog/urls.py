from django.urls import path, include
from .views import HomePageView, post_detalhes, contato_novo

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:post_id>/', post_detalhes, name='detalhes'),
    path('contato', contato_novo, name='comentario_novo'),
]