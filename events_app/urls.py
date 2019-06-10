from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from events_app import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('guests', views.GuestsList.as_view()),
    path('guests/,int:pk/', views.GuestsDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
