from django.urls import path

import views

urlpatterns = [
    path('<pk>/image/', views.AnimalImageLoadView.as_view(), name='animal-image'),
    path('animal-type', views.AnimalTypeViewSet.as_view(), name='animal-type'),
    path('animal-property', views.AnimalPropertyViewSet.as_view(), name='animal-property'),
    path('<pk>/', views.AnimalRetrieveUpdateDestroyView.as_view(), name='animal-detail'),
    path('', views.AnimalListCreateView.as_view(), name='animal-list'),
]
