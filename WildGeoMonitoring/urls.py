from django.urls import path
from WildGeoMonitoring import views
urlpatterns = [
      path('',views.Index,name='index'),

]