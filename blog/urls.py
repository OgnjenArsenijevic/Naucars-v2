from django.urls import path
from .views import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, UserAdListView, SearchResultsListView
from . import views

urlpatterns = [
    path('', AdListView.as_view(), name='blog-home'),
    path('search/', SearchResultsListView.as_view(), name='search-results'),
    path('user/<str:username>', UserAdListView.as_view(), name='user-ads'),
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
    path('ad/new/', AdCreateView.as_view(), name='ad-create'),
    path('ad/<int:pk>/update/', AdUpdateView.as_view(), name='ad-update'),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view(), name='ad-delete'),
    path('about/', views.about, name='blog-about'),
]
