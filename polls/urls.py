from  django.urls import path
# from .views import detail, result, vote
from .views import IndexView, DetailView, ResultsView, vote
app_name = 'polls'

urlpatterns = [
    # path('', index, name="index"),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results', ResultsView.as_view(), name='result'),
    path('<int:question_id>/vote', vote, name='vote'),
]
