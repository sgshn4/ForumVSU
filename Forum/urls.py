from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('views.post/<int:pk>/', views.post_detail, name='post_detail'),
    path('views.post/new/', views.post_create, name='post_create'),
    path('', views.post_list, name='post_list'),
    path('accounts/', include('accounts.urls')),

    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
