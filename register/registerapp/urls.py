from django.urls import path
from registerapp import views
app_name = 'registerapp'
urlpatterns =[
    path('register/' , views.register , name = 'register'),
]
