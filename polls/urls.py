from  django.urls import path
from .views import index, detail, result, vote
urlpatterns = [
    path('', index, name="index"),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:pk>/results', result, name='result'),
    path('<int:pk>/vote', vote, name='vote'),
]