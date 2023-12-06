from django.urls import path, include
from . import views

app_name = 'wwwapp'

urlpatterns = [
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('persons/update/<int:pk>/', views.person_update),
    path('persons/delete/<int:pk>/', views.person_delete),
    path('stanowisko/<int:pk>/members/', views.persons_stanowisko, name='stanowisko'),
    path('test/', views.test_view, name='test'),
]
