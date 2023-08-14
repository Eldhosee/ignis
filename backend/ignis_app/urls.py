from ignis_app import views
from django.urls import path
urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('events', views.events, name='events'),
    path('getevents', views.getevents, name='getevents'),
    path('liked', views.liked, name='liked'),
    path('getliked', views.getliked, name='getliked'),
    path('getlikedevents', views.getlikedevents, name='getlikedevents'),
    path('getcollections', views.getcollections, name='getcollections'),
    path('delete_like/<int:event_id>/', views.delete_like, name='delete_like'),
    
]