from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('detail/<int:question_id>', views.detailview, name = "detail"),
    path('', views.index, name = "index"),
    path('<int:question_id>', views.vote, name = "vote"),
    path('add_question/', views.add_question, name='add_question'),
    path('result/<int:question_id>',views.result, name='result'),
]