from django.urls import path

from django.views.decorators.csrf import csrf_exempt

from api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('posts/', views.Posts.as_view()),
    path('posts/<int:pk>/', views.post_by_id),
    path('posts/<int:pk>/like/', views.put_a_like)
]
